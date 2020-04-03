from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import DetailView 
from django.contrib.auth import get_user_model, authenticate, login, logout 
from django.http import HttpResponseRedirect
from django.views.generic import View
from django.views.generic.edit import FormView
from .models import UserProfile
from .forms import UserRegisterForm, UserForm, ProfileForm
from django.contrib.auth import get_user_model, authenticate, login, logout 

# Create your views here.

User = get_user_model()


class UserRegisterView(FormView):
    template_name = 'accounts/user_register_form.html'
    form_class = UserRegisterForm
    success_url = '/login'

    def form_valid(self, form):
        username = form.cleaned_data.get("username")
        email = form.cleaned_data.get("email")
        password = form.cleaned_data.get("password")
        new_user = User.objects.create(username=username, email=email)
        new_user.set_password(password)
        new_user.save()
        return super(UserRegisterView, self).form_valid(form)



class UserDetailView(DetailView):
    template_name = 'accounts/user_detail.html'
    queryset = User.objects.all() 

    def get_object(self):
        return get_object_or_404(User,
         username__iexact=self.kwargs.get("username")
         )

    def get_context_data(self,*args, **kwargs):
        context = super(UserDetailView, self).get_context_data(*args, **kwargs)
        following = UserProfile.objects.is_following(self.request.user, self.get_object())
        context['following'] = following
        context['recommended'] = UserProfile.objects.recommended(self.request.user)
        return context 



class UserFollowView(View):
    def get(self, request, username, *args, **kwargs):
        toggle_user = get_object_or_404(User, username__iexact=username)
        if request.user.is_authenticated():
            is_following = UserProfile.objects.toggle_follow(request.user, toggle_user)
        return redirect("profiles:detail",username=username)


def loginPage(request):

    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(username=request.POST['username'], password=request.POST['password'])

        
        if user is not None:
            login(request, user)
            return redirect('me')

    context = {}
    return render(request, 'registration/login.html', context)


def logoutPage(request):
    logout(request)
    return redirect('login')


def UserProfileView(request, slug):
    UserProfileView = get_object_or_404(UserProfile, slug=slug)
    context = {
    'UserProfileView' : UserProfileView,
    }
    return render(request, 'accounts/profile.html', context) 


def EditUserProfileView(request, slug):
    EditUserProfileView = get_object_or_404(UserProfile, slug=slug)
    if request.method == 'POST':
        user_form = UserForm(request.POST, instance=request.user)
        profile_form = ProfileForm(request.POST, request.FILES, instance=EditUserProfileView)
        
        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            new_profile = profile_form.save()
            #new_profile.user = request.user
            #new_profile.save()

            return redirect('me')
    else: 
        user_form = UserForm(instance=request.user)
        profile_form = ProfileForm(instance=EditUserProfileView)


    context = {
    'user_form' : user_form,
    'profile_form' : profile_form,
    }

    return render(request, 'accounts/edit_profile.html', context) 