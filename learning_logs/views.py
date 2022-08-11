from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.http import Http404
from .models import Topic, Entry
from .forms import TopicForm, EntryForm

# Create your views here.
def index(request):
    """Learning Log app homepage."""
    return render(request, 'learning_logs/index.html')

def topics(request):
    """Print a list of topics."""
    if request.user.is_authenticated:
        topics = Topic.objects.filter(owner=request.user, public=False).order_by('date_added')
        public_topics = Topic.objects.filter(public=True).order_by('date_added')
        context = {'topics': topics, 'public_topics': public_topics}
        return render(request, 'learning_logs/topics.html', context)
    else:
        public_topics = Topic.objects.filter(public=True).order_by('date_added')
        context = {'public_topics': public_topics}
        return render(request, 'learning_logs/topics.html', context)

def topic(request, topic_id):
    topic = get_object_or_404(Topic, id=topic_id)
    if topic.public == False:
        check_topic_owner(request, topic)
    entries = topic.entry_set.order_by('-date_added')
    context = {'topic': topic, 'entries': entries}
    return render(request, 'learning_logs/topic.html', context)

@login_required
def new_topic(request):
    """Defines a new topic."""
    if request.method != 'POST':
        # No data was sent; create an empty from.
        form = TopicForm()
    else:
        # Sent POST data; process data.
        form = TopicForm(data=request.POST)
        if form.is_valid():
            new_topic = form.save(commit=False)
            new_topic.owner = request.user
            new_topic.save()
            return redirect('learning_logs:topics')

    # Print an empty or invalid form.
    context = {'form': form}
    return render(request, 'learning_logs/new_topic.html', context)

@login_required
def new_entry(request, topic_id):
    """Defines a new entry for specific topic."""
    topic = get_object_or_404(Topic, id=topic_id)
    check_topic_owner(request, topic)
    if request.method != 'POST':
        # No data was sent; create an empty from.
        form = EntryForm()
    else:
        # Sent POST data; process data.
        form = EntryForm(data=request.POST)
        if form.is_valid():
            new_entry = form.save(commit=False)
            new_entry.topic = topic
            new_entry.save()
            return redirect('learning_logs:topic', topic_id=topic_id)

    # Print an empty or invalid form.
    context = {'topic': topic, 'form': form}
    return render(request, 'learning_logs/new_entry.html', context)

@login_required
def edit_entry(request, entry_id):
    """Editing an existing entry."""
    entry = get_object_or_404(Entry, id=entry_id)
    topic = entry.topic
    check_topic_owner(request, topic)

    if request.method != 'POST':
        # Original request; the form is filled with the data of the current record
        form = EntryForm(instance=entry)
    else:
        # Sent POST data; process data.
        form = EntryForm(instance=entry, data=request.POST)
        if form.is_valid():
            form.save()
            return redirect('learning_logs:topic', topic_id=topic.id)

    context = {'entry': entry,'topic': topic, 'form': form}
    return render(request, 'learning_logs/edit_entry.html', context)

@login_required
def delete_entry(request, entry_id):
    """Deleting an existing entry."""
    entry = get_object_or_404(Entry, id=entry_id)
    topic = entry.topic
    check_topic_owner(request, topic)

    if request.method != 'POST':
        # Original request; the form is filled with the data of the current record
        form = EntryForm(instance=entry)
    else:
        # Sent POST data; process data.
        form = EntryForm(instance=entry, data=request.POST)
        if form.is_valid():
            entry.delete()
            return redirect('learning_logs:topic', topic_id=topic.id)

    context = {'entry': entry, 'topic': topic, 'form': form}
    return render(request, 'learning_logs/delete_entry.html', context)


def check_topic_owner(request, topic):
    """Check that the current topic is owned by the current user."""
    if topic.owner != request.user:
        raise Http404