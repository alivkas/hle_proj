import datetime
import time

from django.shortcuts import render, redirect, get_object_or_404
from .models import Project, Tag, Review
from .forms import ProjectForm, ReviewForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.core import paginator
from .utils import paginateProjects, searchProjects


def projects(request):
    projects, search_query = searchProjects(request)
    reviewCount = Review.objects.all()

    if request.user.is_authenticated:
        profile = request.user.profile

        context = {'projects': projects, 'search_query': search_query, 'profile': profile}
        return render(request, 'projects/glavnaya.html', context)

    context = {'projects': projects, 'search_query': search_query, 'review': reviewCount}
    return render(request, 'projects/glavnaya.html', context)


def project(request, project_slug):
    project = Project.objects.get(slug=project_slug)
    tags = project.tags.all()
    form = ReviewForm()

    if request.user.is_authenticated:
        profile = request.user.profile

        if request.method == 'POST' and form.is_valid():
            form = ReviewForm(request.POST)
            review = form.save(commit=False)
            review.project = project
            review.owner = request.user.profile
            review.save()
            project.getVoteCount
            messages.success(request, 'Ваш отзыв был добавлен!')
            return redirect('project', project_slug=project.slug)
        return render(request, 'projects/singleProj.html', {'project': project, 'form': form, 'profile': profile})

    return render(request, 'projects/singleProj.html', {'project': project, 'form': form})


@login_required(login_url="login")
def createProject(request):
    profile = request.user.profile
    form = ProjectForm()

    if request.method == 'POST':
        newtags = request.POST.get('newtags').replace(',',  " ").split()
        form = ProjectForm(request.POST, request.FILES)
        if form.is_valid():
            project = form.save(commit=False)
            project.owner = profile
            project.save()

            for tag in newtags:
                tag, created = Tag.objects.get_or_create(name=tag)
                project.tags.add(tag)
            return redirect('account')

    context = {'form': form, 'profile': profile}
    return render(request, "projects/proj_form.html", context)


@login_required(login_url="login")
def updateProject(request, pk):
    profile = request.user.profile
    project = profile.project_set.get(id=pk)
    form = ProjectForm(instance=project)

    if request.method == 'POST':
        newtags = request.POST.get('newtags').replace(',',  " ").split()

        form = ProjectForm(request.POST, request.FILES, instance=project)
        if form.is_valid():
            project = form.save()
            for tag in newtags:
                tag, created = Tag.objects.get_or_create(name=tag)
                project.tags.add(tag)

            return redirect('account')

    context = {'form': form, 'project': project, 'profile': profile}
    return render(request, "projects/proj_form.html", context)


@login_required(login_url="login")
def deleteProject(request, pk):
    profile = request.user.profile
    project = profile.project_set.get(id=pk)
    if request.method == 'POST':
        project.delete()
        return redirect('account')
    context = {'object': project}
    return render(request, 'delete_template.html', context)


def projects_by_tag(request, tag_slug):
    tag = get_object_or_404(Tag, slug=tag_slug)
    projects = Project.objects.filter(tags__in=[tag])
    context = {
        "projects": projects
    }

    return render(request, "projects/glavnaya.html", context)
