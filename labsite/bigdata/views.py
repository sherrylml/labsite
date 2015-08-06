from django.http import HttpResponse
from django.shortcuts import render, render_to_response
from django.template import RequestContext
from django.utils.translation import LANGUAGE_SESSION_KEY
from .models.models import *
from .models.team_models import Professor, Postgraduate


def index(request):
    '''
    首页
    '''
    Month = {1: 'JAN', 2: 'FEB', 3: 'MAR', 4: 'APR', 5: 'MAY', 6: 'JUN', 7: 'JUL', 8: 'AUG', 9: 'SEP', 10: 'OCT',
             11: 'NOV', 12: 'DEC'}
    news_list = News.objects.all().order_by('-time_stamp')
    if len(news_list) > 3:
        news_list = news_list[0:4]
    notices_list = Notices.objects.all().order_by('-time_stamp')
    if len(notices_list) > 3:
        notices_list = notices_list[0:4]
    meetings_list = Meetings.objects.all()
    join1_list = Join1.objects.order_by('-time_stamp')
    join2_list = Join2.objects.order_by('-time_stamp')
    if len(Lab.objects.all()) > 0:
        lab_intro = Lab.objects.order_by('-id')[0].introduction
    else:
        lab_intro = "Please write the information about lab at first"
        # if request.LANGUAGE_CODE == 'en':
        # return HttpResponse("You prefer to read english.")
        # else:
        # return HttpResponse("You prefer to read another language.")
    return render(request, 'bigdata/index.html', locals())


def index_e(request):
    '''
    首页
    '''
    Month = {1: 'JAN', 2: 'FEB', 3: 'MAR', 4: 'APR', 5: 'MAY', 6: 'JUN', 7: 'JUL', 8: 'AUG', 9: 'SEP', 10: 'OCT',
             11: 'NOV', 12: 'DEC'}
    news_list = News.objects.all().order_by('-time_stamp')
    if len(news_list) > 3:
        news_list = news_list[0:4]
    notices_list = Notices.objects.all().order_by('-time_stamp')
    if len(notices_list) > 3:
        notices_list = notices_list[0:4]
    meetings_list = Meetings.objects.all()
    join1_list = Join1.objects.order_by('-time_stamp')
    join2_list = Join2.objects.order_by('-time_stamp')
    if len(Lab.objects.all()) > 0:
        lab_intro = Lab.objects.order_by('-id')[0].introduction
    else:
        lab_intro = "Please write the information about lab at first"
    # print(request.session[LANGUAGE_SESSION_KEY])
    return render(request, 'bigdata/index_e.html', locals())
    # return render_to_response('bigdata/index_e.html', locals(), RequestContext(request))


def news(request):
    '''
    通知&新闻
    '''
    news_list = News.objects.order_by('-time_stamp')
    notices_list = Notices.objects.order_by('-time_stamp')
    return render_to_response('bigdata/news.html', locals())


def news_detail(request, id):
    '''
    新闻详情
    '''
    item_id = int(id)
    size = News.objects.all().count() - 1
    first = News.objects.all()[0].id
    last = News.objects.all()[size].id

    if item_id == first:
        has_previous = False
        previous_id = item_id
    else:
        has_previous = True
        previous_id = item_id - 1
        while not News.objects.filter(id=previous_id).count():
            previous_id -= 1

    if item_id == last:
        has_next = False
        next_id = item_id
    else:
        has_next = True
        next_id = item_id + 1
        while not News.objects.filter(id=next_id).count():
            next_id += 1

    news = News.objects.get(id=item_id)
    Month = {1: 'JAN', 2: 'FEB', 3: 'MAR', 4: 'APR', 5: 'MAY', 6: 'JUN', 7: 'JUL', 8: 'AUG', 9: 'SEP', 10: 'OCT',
             11: 'NOV', 12: 'DEC'}
    Context = {'news': news, 'Month': Month, 'has_previous': has_previous, 'has_next': has_next,
               'previous_id': previous_id, 'next_id': next_id}
    return render_to_response('bigdata/news_detail.html', Context)


def notice_detail(request, id):
    '''
    通知详情
    '''
    item_id = int(id)
    size = Notices.objects.all().count() - 1
    first = Notices.objects.all()[0].id
    last = Notices.objects.all()[size].id

    if item_id == first:
        has_previous = False
        previous_id = item_id
    else:
        has_previous = True
        previous_id = item_id - 1
        while not Notices.objects.filter(id=previous_id).count():
            previous_id -= 1

    if item_id == last:
        has_next = False
        next_id = item_id
    else:
        has_next = True
        next_id = item_id + 1
        while not Notices.objects.filter(id=next_id).count():
            next_id += 1

    notice = Notices.objects.get(id=item_id)
    Month = {1: 'JAN', 2: 'FEB', 3: 'MAR', 4: 'APR', 5: 'MAY', 6: 'JUN', 7: 'JUL', 8: 'AUG', 9: 'SEP', 10: 'OCT',
             11: 'NOV', 12: 'DEC'}
    Context = {'notice': notice, 'Month': Month, 'has_previous': has_previous, 'has_next': has_next,
               'previous_id': previous_id, 'next_id': next_id}
    return render_to_response('bigdata/notice_detail.html', Context)


def team(request):
    '''
    科研团队
    '''
    professors_list = Professor.objects.all()
    masters_list = Postgraduate.objects.filter(educational_level='master')
    doctors_list = Postgraduate.objects.filter(educational_level='master')
    return render_to_response('bigdata/team.html', locals())


def member_professor(request, id):
    '''
    个人主页
    '''
    item_id = int(id)
    member = Professor.objects.get(id=item_id)
    researchDir_list = member.resdir_set.all()
    workExp_list = member.workexp_set.all()
    patentPri_list = member.patpri_set.all()
    publishInf_list = member.pubinf_set.all()
    researchAct_list = member.resact_set.all()
    return render_to_response('bigdata/member.html', locals())


def member_postgraduate(request, id):
    '''
    个人主页
    '''
    item_id = int(id)
    member = Postgraduate.objects.get(id=item_id)
    researchDir_list = member.resdir1_set.all()
    workExp_list = member.workexp1_set.all()
    patentPri_list = member.patpri1_set.all()
    publishInf_list = member.pubinf1_set.all()
    researchAct_list = member.resact1_set.all()
    return render_to_response('bigdata/member.html', locals())


class ResearchDirection():
    def __init__(self, direction, images):
        self.direction = direction
        self.images = images


def research(request):
    '''
    科学研究
    '''
    direction_list = []
    if len(Lab.objects.all()) > 0:
        research_directions = Lab.objects.order_by('-id')[0].directions_set.all()
        for research_direction in research_directions:
            direction_images = research_direction.images_set.all()
            direction_list.append(ResearchDirection(research_direction.research_direction, direction_images))
        research_achievement = Lab.objects.order_by('-id')[0].achievement
    else:
        research_achievement = " "
    Context = {'direction_list': direction_list, 'research_achievement': research_achievement}
    return render_to_response('bigdata/research.html', Context)


def academic(request):
    '''
    合作交流
    '''
    academic_list = Academic.objects.all()
    meetings_list = Meetings.objects.all()
    return render_to_response('bigdata/academic.html', locals())


def academic_detail(request, id):
    '''
    学术交流活动详情
    '''
    item_id = int(id)
    size = Academic.objects.all().count() - 1
    first = Academic.objects.all()[0].id
    last = Academic.objects.all()[size].id

    if item_id == first:
        has_previous = False
        previous_id = item_id
    else:
        has_previous = True
        previous_id = item_id - 1
        while not Academic.objects.filter(id=previous_id).count():
            previous_id -= 1

    if item_id == last:
        has_next = False
        next_id = item_id
    else:
        has_next = True
        next_id = item_id + 1
        while not Academic.objects.filter(id=next_id).count():
            next_id += 1

    academic = Academic.objects.get(id=item_id)
    Month = {1: 'JAN', 2: 'FEB', 3: 'MAR', 4: 'APR', 5: 'MAY', 6: 'JUN', 7: 'JUL', 8: 'AUG', 9: 'SEP', 10: 'OCT',
             11: 'NOV', 12: 'DEC'}
    Context = {'academic': academic, 'Month': Month, 'has_previous': has_previous, 'has_next': has_next,
               'previous_id': previous_id, 'next_id': next_id}
    return render_to_response('bigdata/academic_detail.html', Context)


def relax(request, id):
    '''
    活动休闲
    '''
    curr_page = int(id)
    size = Relax.objects.all().count()
    if size % 5 == 0:
        all_page = size // 5
    else:
        all_page = size // 5 + 1
    start_pos = (curr_page - 1) * 5
    end_pos = start_pos + 5
    if size < end_pos:
        end_pos = size
    if curr_page == 1:
        has_previous = False
    else:
        has_previous = True
    if curr_page == all_page:
        has_next = False
    else:
        has_next = True
    previous_page = curr_page - 1
    next_page = curr_page + 1
    relax_list = Relax.objects.all()[start_pos: end_pos]
    Month = {1: 'JAN', 2: 'FEB', 3: 'MAR', 4: 'APR', 5: 'MAY', 6: 'JUN', 7: 'JUL', 8: 'AUG', 9: 'SEP', 10: 'OCT',
             11: 'NOV', 12: 'DEC'}
    Context = {'relax_list': relax_list, 'Month': Month, 'has_next': has_next, 'has_previous': has_previous,
               'previous_page': previous_page, 'next_page': next_page}
    return render(request, 'bigdata/relax.html', Context)


def join(request):
    '''
    加入我们
    '''
    join1_list = Join1.objects.order_by('-time_stamp')
    join2_list = Join2.objects.order_by('-time_stamp')
    return render(request, 'bigdata/join.html', locals())


def about(request):
    '''
    关于
    '''
    lab = Lab.objects.order_by('-id')[0]
    lab_intro = lab.introduction
    Context = {'lab_intro': lab_intro}
    return render(request, 'bigdata/about.html', Context)


