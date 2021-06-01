from django.urls import path

from notes import views


urlpatterns = [

    path(
        route='', 
        view=views.FeedView.as_view(), 
        name='feed',
    ),
    path(
        route='notes/new/', 
        view=views.NewNoteView.as_view(), 
        name='new',
    ),
    path(
        route='notes/edit/<int:note_pk>',
        view=views.EditNoteView.as_view(),
        name='edit',
    ),
    path(
        route='notes/delete/<int:note_pk>',
        view=views.DeleteNoteView.as_view(),
        name='delete',
    ),
    
]