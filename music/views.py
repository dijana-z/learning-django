from django.views import generic
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import View
from django.urls import reverse_lazy
from django.shortcuts import render, redirect
from django.contrib.auth import  authenticate, login
from .models import Album
from .forms import UserForm


class IndexView(generic.ListView):
    # defining which template we will be using
    template_name = 'music/index.html'
    context_object_name = 'all_albums'

    def get_queryset(self):
        """
        :return: returns all albums from database
        """
        return Album.objects.all()


class DetailView(generic.DetailView):
    # defining what are we trying to get
    model = Album
    # defining which template we will be using
    template_name = 'music/detail.html'


class AlbumCreate(CreateView):
    # what you are trying to create
    model = Album
    # mandatory fields
    fields = ['artist', 'album_title', 'genre', 'album_logo']


class AlbumUpadte(UpdateView):
    # what you are trying to update
    model = Album
    # mandatory fields
    fields = ['artist', 'album_title', 'genre', 'album_logo']


class AlbumDelete(DeleteView):
    # what you are trying to delete
    model = Album
    # where to go after the album is deleted
    success_url = reverse_lazy('music:index')


class UserFormView(View):
    # what is the blueprint that you are going to use for the form?
    form_class = UserForm
    # html file that the form is going to be included in
    template_name = 'music/registration_form.html'

    def get(self, request):
        """
        going to display a blank form for signing up
        """
        # by the default it has no data, the user is meant to fill the blanks
        form = self.form_class(None)
        return render(request, self.template_name, {'form': form})

    def post(self, request):
        """
        process form data and save our user to the database
        """
        # this time we need to send the post request instead of nothing
        # that is the information that is typed into the form
        # and after submitting all of the data will be stored in this POST data
        # that we will pass to the form and the form itself will validate the data
        form = self.form_class(request.POST)
        if form.is_valid():
            # creates an object from the form without saving it so we can validate even more
            user = form.save(commit=False)

            # cleaned (normalized) data
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            # NOTE: if the username needs changing, change it with user.username = 'New Username'
            #       but if the password needs changing, you must change it with user.set_password('new password')
            user.username = username
            user.set_password(password)
            user.save()

            # returns User object if the credentials are correct
            user = authenticate(username=username, password=password)
            if user:
                # if the user is not banned
                if user.is_active:
                    # logging in
                    login(request, user)
                    # after the login redirect them to the home page
                    return redirect('music:index')

        # if they didn't login, try again
        return render(request, self.template_name, {'form': form})


