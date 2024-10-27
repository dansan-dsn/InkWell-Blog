from django.shortcuts import get_object_or_404, render, redirect
from . models import User
from django.contrib.auth.hashers import make_password, check_password

# requres login
def login_required(view_func):
    def _wrapped_view(request, *args, **kwargs):
        if 'user_id' not in request.session:
            return redirect('users:login')  # Adjust the URL name as per your routing
        return view_func(request, *args, **kwargs)
    return _wrapped_view

# user registration
def register_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        is_author = request.POST.get('is_author') == 'on'  # Boolean
        password = request.POST.get('password')

        print(f"Username: {username}, Email: {email}, is_author: {is_author}, Password: {password}")
        
        # Check for username and email existence
        if User.objects.filter(username=username).exists():
            return render(request, 'register.html', {'error': "Username already taken"})
        if User.objects.filter(email=email).exists():
            return render(request, 'register.html', {'error': "Email in use"})
        
        # Password validation
        if len(password) < 6:
            return render(request, 'register.html', {'error': "Password must be at least 6 characters long."})

        # Hash the password and create user
        hash_password = make_password(password)
        role = 'author' if is_author else 'guest'
        user = User.objects.create(username=username, email=email, role=role, password=hash_password)
        
        print("User created:", user)

        # Redirect to login page after successful registration
        return redirect('users:login')

    return render(request, 'register.html')

# user login
def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        
        try:
            # Retrieve the user by username
            user = User.objects.get(username=username)

            print(f"Logging in user: {username}")
            # Check if the provided password matches the stored hashed password
            if check_password(password, user.password):
                print(f"User authenticated: {user.username}")
                # Password is correct; log the user in (you might want to set a session)
                request.session['user_id'] = user.id
                request.session['username'] = user.username 
                request.session['role'] = user.role
                return redirect(f"/?username={user.username}&role={user.role}")
            else:
                return render(request, 'login.html', {'error': "wrong password"})
        
        except User.DoesNotExist:
            # User does not exist
            return render(request, 'login.html', {'error': "User does not exist"})

    return render(request, 'login.html')


# user password reset
def forgot_password(request):
    return render(request, 'forgot_password.html')


@login_required
def all_users(request):
    users = User.objects.all()
    return render(request, 'all_users.html', {'users': users})


@login_required
def single_user(request, pk):
    # Retrieve the user by primary key
    user = get_object_or_404(User, pk=pk)
    
    # Render a template with the user data
    return render(request, 'single_user.html', {'user': user})


@login_required
def logout_view(request):
    request.session.flush()  # Clear all session data
    return redirect('home')