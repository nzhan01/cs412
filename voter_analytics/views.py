# voter_analytics/views.py
# Nicholas Zhang
# nzhan01@bu.edu
# created: 10/31/2025
# models file containing all the views for the voter_analytics app

from django.shortcuts import render

# Create your views here.

from django.db.models.query import QuerySet
from django.views.generic import ListView, DetailView ## NEW
from . models import Voter
 ## new imports: for the plotly library
import plotly
import plotly.graph_objs as go
from datetime import date

class ResultsListView(ListView):
    ''' view to display voter information'''
    template_name = 'voter_analytics/results.html'
    model = Voter
    context_object_name = 'results'
    paginate_by = 100
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['years'] = range(1920, 2005) #for max and min DOB filters
        context['result_count'] = self.get_queryset().count()
        context['filters'] = self.request.GET # to retain filter values in template
        context['form_action'] = 'voter_list' 
        params = self.request.GET.copy()
        if 'page' in params:
            params.pop('page')
        context['querystring'] = params.urlencode()
        return context


    def get_queryset(self):
        
        # start with entire queryset
        results = super().get_queryset().order_by('first_name')
 
 
        # filter results by these field(s):
        # party_affiliation
        if 'party_affiliation' in self.request.GET:
            party = self.request.GET['party_affiliation']
            if party:
                results = results.filter(party_affiliation=party)
                
        # voter_score
        if 'voter_score' in self.request.GET:
            score = self.request.GET['voter_score']
            if score:
                results = results.filter(voter_score=score)

        # election participation
        if 'v20state' in self.request.GET:
            v20state_value = self.request.GET['v20state']
            if v20state_value:
                results = results.filter(v20state="True")
        if 'v21town' in self.request.GET:
            v21town = self.request.GET['v21town']
            if v21town:
                results = results.filter(v21town='True')

        if 'v21primary' in self.request.GET:
            v21primary = self.request.GET['v21primary']
            if v21primary:
                results = results.filter(v21primary='True')
        if 'v22general' in self.request.GET:
            v22general = self.request.GET['v22general']
            if v22general:
                results = results.filter(v22general='True')

        if 'v23town' in self.request.GET:
            v23town = self.request.GET['v23town']
            if v23town:
                results = results.filter(v23town='True')

        
        
        if 'min_year' in self.request.GET:
            min_year = self.request.GET['min_year']
            
            if min_year:
                min_year = int(min_year) 
                min_date = date(min_year, 1, 1)
                results = results.filter(date_of_birth__gte=min_date)
    
        if 'max_year' in self.request.GET:
            max_year = self.request.GET['max_year']
            
            if max_year:
                max_year = int(max_year) 
                max_date = date(max_year, 12, 31)
                results = results.filter(date_of_birth__lte=max_date)
        return results
    


class ResultDetailView(DetailView):
    '''View to show detail page for one result.'''
 
 
    template_name = 'voter_analytics/voter_detail.html'
    model = Voter
    context_object_name = 'r'

    def get_context_data(self, **kwargs):
        '''
        Provide context variables for use in template
        '''
        # start with superclass context
        context = super().get_context_data(**kwargs)
        r = context['r']
        




        return context
    

class GraphsView(ListView):
    '''view to display graphs of voter analytics'''
    template_name = 'voter_analytics/graphs.html'
    model = Voter
    context_object_name = 'r'

    def get_queryset(self):
        
        # start with entire queryset
        results = super().get_queryset().order_by('first_name')
 
 
        # filter results by these field(s):
        # party_affiliation
        if 'party_affiliation' in self.request.GET:
            party = self.request.GET['party_affiliation']
            if party:
                results = results.filter(party_affiliation=party)
                
        # voter_score
        if 'voter_score' in self.request.GET:
            score = self.request.GET['voter_score']
            if score:
                results = results.filter(voter_score=score)

        # election participation
        if 'v20state' in self.request.GET:
            v20state_value = self.request.GET['v20state']
            if v20state_value:
                results = results.filter(v20state="True")
        if 'v21town' in self.request.GET:
            v21town = self.request.GET['v21town']
            if v21town:
                results = results.filter(v21town='True')

        if 'v21primary' in self.request.GET:
            v21primary = self.request.GET['v21primary']
            if v21primary:
                results = results.filter(v21primary='True')
        if 'v22general' in self.request.GET:
            v22general = self.request.GET['v22general']
            if v22general:
                results = results.filter(v22general='True')

        if 'v23town' in self.request.GET:
            v23town = self.request.GET['v23town']
            if v23town:
                results = results.filter(v23town='True')

        
        
        if 'min_year' in self.request.GET:
            min_year = self.request.GET['min_year']
            
            if min_year:
                min_year = int(min_year) 
                min_date = date(min_year, 1, 1)
                results = results.filter(date_of_birth__gte=min_date)
    
        if 'max_year' in self.request.GET:
            max_year = self.request.GET['max_year']
            
            if max_year:
                max_year = int(max_year) 
                max_date = date(max_year, 12, 31)
                results = results.filter(date_of_birth__lte=max_date)
        return results

    def get_context_data(self, **kwargs):
        '''
        Provide context variables for use in template
        '''
        # start with superclass context
        context = super().get_context_data(**kwargs)
        context['years'] = range(1920, 2005) #for max and min DOB filters
        context['result_count'] = self.get_queryset().count()
        context['filters'] = self.request.GET # to retain filter values in template
        context['form_action'] = 'graphs'

        r = context['r']
        
        
        # create graph of voter party affiliation as pie chart:
        x=[]
        y=[]
        for voter in r:
            if voter.party_affiliation not in x:
                x.append(voter.party_affiliation)
                y.append(1)

            else:
                index = x.index(voter.party_affiliation)
                y[index] += 1
        # generate the Pie chart
        fig = go.Pie(labels=x, values=y) 
        title_text = "Voter Party Distribution"
        # obtain the graph as an HTML div"
        graph_div_voter_distribution = plotly.offline.plot({"data": [fig], "layout_title_text": title_text, }, 
        auto_open=False, 
        output_type="div")
        # send div as template context variable
        context['graph_div_voter_distribution'] = graph_div_voter_distribution



        
         # create graph of voter distribution by year of birth as bar chart:
        x=[]
        y=[]
        for voter in r:
            if voter.date_of_birth.year not in x:
                x.append(voter.date_of_birth.year)
                y.append(1)

            else:
                index = x.index(voter.date_of_birth.year)
                y[index] += 1
        
        
        fig = go.Bar(x=x, y=y)
        title_text = f"Voter Distribution by Year of Birth"
        graph_div_dob_year = plotly.offline.plot({"data": [fig], 
                                         "layout_title_text": title_text,
                                         }, auto_open=False, output_type="div",               
                                         ) 
        context['graph_div_dob_year'] = graph_div_dob_year
       
       # create graph of voter distribution by participation in elections as bar chart:
        x=['v20state', 'v21town', 'v21primary', 'v22general', 'v23town']
        y=[0,0,0,0,0]
        for voter in r:
            for field in x:
                if field == 'v20state' and voter.v20state:
                    y[0] += 1
                if field == 'v21town' and voter.v21town:
                    y[1] += 1
                if field == 'v21primary' and voter.v21primary:
                    y[2] += 1
                if field == 'v22general' and voter.v22general:
                    y[3] += 1
                if field == 'v23town' and voter.v23town:
                    y[4] += 1
        
        
        fig = go.Bar(x=x, y=y)
        title_text = f"Voter Distribution by Election Participation"
        graph_div_election_participation = plotly.offline.plot({"data": [fig], 
                                         "layout_title_text": title_text,
                                         }, auto_open=False, output_type="div",               
                                         ) 
        context['graph_div_election_participation'] = graph_div_election_participation
       
        




        return context