from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm

# Create your views here.
def register(request):
    """Registers a new user."""
    if request.method != 'POST':
        # Print an empty form of registration.
        form = UserCreationForm()
    else:
        # Processing the completed form.
        form = UserCreationForm(data=request.POST)

        if form.is_valid():
            new_user = form.save()
            # Accepting login and redirect to homepage.
            login(request, new_user)
            return redirect('learning_logs:index')

    # Print an empty or invalid form.
    context = {'form': form}
    return render(request, 'registration/register.html', context)