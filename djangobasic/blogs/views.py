from django.shortcuts import render
# Create your views here.
def hello(request):
    tags = ['เพลง','ภาพยนต์','สุขภาพ','กีฬา']
    rating = 4
    return render(request,'index.html',
    {
        'name':'บทความ',
        'author':'Linda',
        'tags':tags,
        'rating':rating
    })
