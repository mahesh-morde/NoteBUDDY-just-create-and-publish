from django.http import JsonResponse
from django.shortcuts import render,redirect,get_object_or_404
from .models import *
from authh.models import *
from django.contrib.auth import authenticate
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.db.models import Q
from django.core.files.storage import FileSystemStorage

# Create your views here.
def index(request):
    return render(request, 'index.html')

def about(request):
    return render(request, 'about.html')


def dashboard(request):
    if not request.user.is_authenticated:
        return redirect('user_login')

    user = request.user
    try:
        signup = Signup.objects.get(user=user)
        totalnotes = Notes.objects.filter(signup=signup).count()
    except Signup.DoesNotExist:
        signup = None
        totalnotes = 0

    # Assuming you want 5 notes per page
    notes_list = Notes.objects.filter(publish=True)

    # Search functionality
    query = request.GET.get('q')
    if query:
        notes_list = notes_list.filter(Q(Title__icontains=query))

    paginator = Paginator(notes_list, 5)  # Show 5 notes per page

    page = request.GET.get('page')
    try:
        notes = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        notes = paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
        notes = paginator.page(paginator.num_pages)

    return render(request, 'dashboard.html', locals())

# def addNotes(request):
#     if not request.user.is_authenticated:
#         return redirect('user_login')
#     user = User.objects.get(id=request.user.id)
#     signup = Signup.objects.get(user=user)

#     error = ""
#     if request.method == "POST":
#         title = request.POST['Title']
#         content = request.POST['content_from_file']
        
#         try:
#             Notes.objects.create(signup=signup, Title=title, Content=content)
#             print()
#             error = "no"
#         except:
#             error = "yes"
#     return render(request, 'addNotes.html', locals())

from django.utils.html import escape

# ... (existing imports) ...

def addNotes(request):
    if not request.user.is_authenticated:
        return redirect('user_login')
    
    user = User.objects.get(id=request.user.id)
    signup = Signup.objects.get(user=user)

    error = ""
    content_from_file = ""

    if request.method == "POST":
        title = request.POST['Title']
        content = request.POST.get('Content', '')

        if 'extract' in request.POST:
            # Extract content from the uploaded file
            uploaded_file = request.FILES.get('file')
            if uploaded_file:
                fs = FileSystemStorage()
                filename = fs.save(uploaded_file.name, uploaded_file)

                with fs.open(filename) as file:
                    content_from_file = file.read().decode('utf-8')

                return JsonResponse({'success': True, 'content': content_from_file})

        try:
            # Save the content as HTML (escaped for security)
            Notes.objects.create(signup=signup, Title=title, Content=escape(content))
            error = "no"
        except:
            error = "yes"

    return render(request, 'addNotes.html', {'content_from_file': content_from_file, 'error': error})


def viewNotes(request):
    if not request.user.is_authenticated:
        return redirect('user_login')
    user = User.objects.get(id=request.user.id)
    signup = Signup.objects.get(user=user)
    notes = Notes.objects.filter(signup=signup)
    return render(request, 'viewNotes.html', locals())

def editNotes(request,pid):
    if not request.user.is_authenticated:
        return redirect('user_login')
    notes = Notes.objects.get(id=pid)
    if request.method == "POST":
        title = request.POST['Title']
        content = request.POST['Content']

        notes.Title = title
        notes.Content = content

        try:
            notes.save()
            error = "no"
        except:
            error = "yes"
    return render(request, 'editNotes.html', locals())

def deleteNotes(request,pid):
    if not request.user.is_authenticated:
        return redirect('user_login')
    notes = Notes.objects.get(id=pid)
    notes.delete()
    return redirect('viewNotes')


def publish_note(request, pid):
    if not request.user.is_authenticated:
        return redirect('user_login')

    note = get_object_or_404(Notes, id=pid)
    note.publish = True
    note.save()

    return redirect('viewNotes')

def unpublish_note(request, pid):
    if not request.user.is_authenticated:
        return redirect('user_login')

    note = get_object_or_404(Notes, id=pid)
    note.publish = False
    note.save()

    return redirect('viewNotes')





 