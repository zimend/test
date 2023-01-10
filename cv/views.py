from django.shortcuts import render
from django.http import HttpResponse
from django.views import generic
from django.views.generic import DetailView
from cv.models import *
from resume.context_processors import project_context
# =======================================

from . form import ContactForm
from django.contrib import messages


class IndexView(generic.FormView):
    template_name = "cv.html"
    form_class = ContactForm
    success_url = "/"

    def form_valid(self, form, **kwargs):
        context = super().get_context_data(**kwargs)
        connected_user = project_context(request=self.request)['the_hero']
        connected_profile = UserProfile.objects.filter(user_id = connected_user.pk)[0]
        form = form.save(commit=False)
        form.profile = connected_profile
        form.save()
        messages.success(self.request, 'Thank you. We will be in touch soon.')
        return super().form_valid(form)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)      
        connected_user=project_context(request=self.request)['the_hero']
        if connected_user!=None:
            i_am = I_Am.objects.filter(profile=connected_user.pk)
            sections = Section.objects.filter(is_active=True).filter(profile=connected_user.pk)
            facts = Fact.objects.filter(is_active=True).filter(profile=connected_user.pk)
            skills = Skill.objects.filter(profile=connected_user.pk)
        
            resumes = Resume.objects.filter(profile=connected_user.pk)
            context["categoriesResume"] = CategoriesResume.choices
            works = {}
            for cv in resumes:           
                works[cv.pk] = Works.objects.filter(resume=cv.pk)
        
            context["works"] = works

        
            portfolio = Portfolio.objects.filter(is_active=True).filter(profile=connected_user.pk)
            qurey_categoriesPortfolio = portfolio.values('category')
            categoriesPortfolio = set( val for dic in qurey_categoriesPortfolio for val in dic.values() )
            # categoriesPortfolio = set( val for dic in qurey_categoriesPortfolio for val in dic.values())
            context["categoriesPortfolio"] = categoriesPortfolio
            testimonials = Testimonial.objects.filter(is_active=True).filter(profile=connected_user.pk)
            certificates = Certificate.objects.filter(is_active=True).filter(profile=connected_user.pk) 

            context['i_am'] = i_am
            context["sections"] = sections
            context["facts"] = facts
            context["skills"] = skills
            context["resume"] = resumes
            context["testimonials"] = testimonials
            context["certificates"] = certificates
            context["portfolio"] = portfolio
        return context


class PortfolioDetailView(generic.DetailView):
	
    model = Portfolio
    template_name = "portfolio-details.html"
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)      
        gallery = ScreenShotsPortfolio.objects.select_related('portfolio').filter(portfolio=kwargs['object'])
        context["gallery"]= gallery
        return context
     

    

    
    