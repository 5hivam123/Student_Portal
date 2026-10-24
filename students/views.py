from django.shortcuts import render

def student_home(request):
    students = [
        {"name": "Rahul", "course": "B.Tech CSE", "marks": 85},
        {"name": "Aman", "course": "B.Tech AIML", "marks": 32},
        {"name": "Priya", "course": "B.Tech IT", "marks": 76},
    ]

    context = {
        "students": students
    }

    return render(request, "students/home.html", context)


def about_page(request):
    return render(request, "students/about.html")