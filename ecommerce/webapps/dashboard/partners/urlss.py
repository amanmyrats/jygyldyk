from django.urls import path

from .views import (
    PartnerListView, PartnerCreateView, PartnerManageView, PartnerDeleteView, 
    PartnerUserLinkView, PartnerUserUnlinkView, PartnerUserCreateView, 
    PartnerUserSelectView, PartnerUserUpdateView
)


list_view = PartnerListView
create_view = PartnerCreateView
manage_view = PartnerManageView
delete_view = PartnerDeleteView

user_link_view = PartnerUserLinkView
user_unlink_view = PartnerUserUnlinkView
user_create_view = PartnerUserCreateView
user_select_view = PartnerUserSelectView
user_update_view = PartnerUserUpdateView

urlpatterns = [
    path('', list_view.as_view(), name='partner-list'),
    path('create/', create_view.as_view(), name='partner-create'),
    path('<int:pk>/', manage_view.as_view(), name='partner-manage'),
    path('<int:pk>/delete/', delete_view.as_view(), name='partner-delete'),

    path('<int:partner_pk>/users/add/', user_create_view.as_view(), name='partner-user-create'),
    path('<int:partner_pk>/users/select/', user_select_view.as_view(), name='partner-user-select'),
    path(
        '<int:partner_pk>/users/<int:user_pk>/link/',
        user_link_view.as_view(), name='partner-user-link'),
    path(
        '<int:partner_pk>/users/<int:user_pk>/unlink/',
        user_unlink_view.as_view(), name='partner-user-unlink'),
    path(
        '<int:partner_pk>/users/<int:user_pk>/update/',
        user_update_view.as_view(),
        name='partner-user-update'),
]
