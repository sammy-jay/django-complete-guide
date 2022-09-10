from django.shortcuts import render, get_object_or_404
from django.contrib.auth import get_user_model

from .models import Board, Post
from .forms import NewTopicForm

User = get_user_model()


def home(request):
    boards = Board.objects.all()
    return render(request, 'boards/home.html', {'boards': boards})


def board_topics(request, pk):
    board = get_object_or_404(Board, pk=pk)
    return render(request, 'boards/topics.html', {'board': board})


def new_topic(request, pk):
    board = get_object_or_404(Board, pk=pk)
    user = User.objects.first()

    if request.method == 'POST':
        form = NewTopicForm(request.POST)
        if form.is_valid():
            topic = form.save(commit=False)
            topic.board = board
            topic.starter = user
            topic.save()

            post = Post.objects.create(
                topic=topic, message=form.cleaned_data.get('message'), created_by=user)

            return redirect('boards:board_topics', kwargs={'pk': board.pk})

    form = NewTopicForm()
    return render(request, 'boards/new_topic.html', {'board': board, 'form': form})
