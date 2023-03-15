from django.shortcuts import render

posts=[
{
    'author':'Chew',
    'title':'Blog Post 1',
    'content':'First post content',
    'date_posted':'August 27, 2018'
},
{
    'author':'Yong',
    'title':'Blog Post 2',
    'content':'Second post content',
    'date_posted':'August 28, 2018'
}

]




def Home(request):
    context={
        "postss":posts}
    return render(request,'blog/home.html',context )

def about(request):

    return render(request,'blog/about.html',{"title":'About'})

