from django.shortcuts import render, get_object_or_404, redirect
from .models import Board, Topic
from .forms import topicform, postform
from django.contrib.auth.decorators import login_required
from django.db.models import Count
from django.utils import timezone

from django.core.paginator import PageNotAnInteger,Paginator,EmptyPage


def home(request):
    boards = Board.objects.all()
    return render(request, 'home.html', {'boards': boards})

def topiclist(request,pk):
    board=get_object_or_404(Board,pk=pk)
    queryset=board.topics.order_by('-last_updated').annotate(replies=Count('posts')-1)
    page=request.GET.get('page',1)
    paginator=Paginator(queryset,10)
    try:
        topics=paginator.page(page)
    except PageNotAnInteger:
        topics=paginator.page(1)
    except EmptyPage:
        topics=paginator.page(paginator.num_pages)
    return render(request,'topics.html',{'topics':topics,'board':board})

def postlist(request,pk,topic_pk):
    topic=get_object_or_404(Topic,board__pk=pk,pk=topic_pk)
    session_key='viewed_topic_{}'.format(topic.pk)
    if not request.session.get(session_key,False):
        topic.views += 1
        topic.save()
        request.session[session_key]=True
    queryset=topic.posts.order_by('created_by')
    page=request.GET.get('page',1)
    paginator=Paginator(queryset,10)
    try:
        posts=paginator.page(page)
    except PageNotAnInteger:
        posts=paginator.page(1)
    except EmptyPage:
        posts=paginator.page(paginator.num_pages)
    return render(request,'topic_posts.html',{'topic':topic,'posts':posts})


@login_required
def newtopic(request, pk):
    board = get_object_or_404(Board, pk=pk)
    if request.method != 'POST':
        form = topicform()
    else:
        form = topicform(data=request.POST)
        if form.is_valid():
            newtopic = form.save(commit=False)
            newtopic.starter = request.user
            newtopic.board = board
            newtopic.save()
            return redirect('appone:topic_posts', pk=board.pk, topic_pk=newtopic.pk)
    return render(request, 'newtopic.html', {'board': board, 'form': form})


@login_required
def reply_topic(request, pk, topic_pk):
    topic = get_object_or_404(Topic, board__pk=pk, pk=topic_pk)
    if request.method != 'POST':
        form = postform()
    else:
        form = postform(data=request.POST)
        if form.is_valid():
            new_post = form.save(commit=False)
            new_post.topic = topic
            new_post.created_by = request.user
            new_post.save()
            topic.last_updated=timezone.now()
            topic.save()
            return redirect('appone:topic_posts', pk=pk, topic_pk=topic_pk)
    return render(request, 'reply_topic.html', {'form': form, 'topic': topic})


@login_required()
def edit_post(request,pk,topic_pk,post_pk):
    board=Board.objects.get(pk=pk)
    topic=board.topics.get(pk=topic_pk)
    post=topic.posts.get(pk=post_pk)
    if request.method!='POST':
        form=postform(instance=post)
    else:
        form=postform(instance=post,data=request.POST)
        post=form.save(commit=False)
        post.updated_at=timezone.now()
        post.updated_by=request.user
        post.save()
        return redirect('appone:topic_posts',pk=post.topic.board.pk,topic_pk=post.topic.pk)
    return render(request,'edit_post.html',{'post':post,'form':form})
