from django.shortcuts import render
from .models import Project, ActiveThought


def index(request):
    context = {
        'projects': Project.objects.all(),
        'latest_thought': ActiveThought.objects.first(),
    }
    return render(request, 'portfolio/landing.html', context)


# def index(request):
#     mock_projects = [
#         {
#             "id": 1,
#             "title": "Invoicing System",
#             "subtitle": "Building a custom invoicing engine with using Python, Tailwind CSS, BigQuery and Stripe integration.",
#             "role": "Developer",
#             "timeline": "2026",
#             "impact_metric": "+150 Aura",
#             "description": "Implemented complex security and transaction tracking for processing corporate payroll profiles.",
#         },
#         {
#             "id": 2,
#             "title": "OninApps",
#             "subtitle": "blah blah blah",
#             "role": "Developer",
#             "timeline": "2026",
#             "impact_metric": "100% satisfaction",
#             "description": "created a portal that allows clients to view invoicing data, make payments and see other client specific data.",
#         },
#         {
#             "id": 3,
#             "title": "Biometic timekeeping ",
#             "subtitle": "blah blah blah",
#             "role": "Developer",
#             "timeline": "2026",
#             "impact_metric": "100% satisfaction",
#             "description": "noahface filler text",
#         },
#         {
#             "id": 3,
#             "title": "flex / connecteam ",
#             "subtitle": "blah blah blah",
#             "role": "Developer",
#             "timeline": "2026",
#             "impact_metric": "100% satisfaction",
#             "description": "noahface filler text",
#         },
#         {
#             "id": 3,
#             "title": "frontend work",
#             "subtitle": "blah blah blah",
#             "role": "Developer",
#             "timeline": "2026",
#             "impact_metric": "100% satisfaction",
#             "description": "noahface filler text",
#         },
#     ]
#
#     mock_thought = {
#         "phrase": "Welcome to my portfolio!",
#         "phrase1": "Click around and make yourself at home"
#     }
#
#     context = {
#         'projects': mock_projects,
#         'latest_thought': mock_thought,
#     }
#     return render(request, 'portfolio/landing.html', context)