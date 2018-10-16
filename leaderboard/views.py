from django.http import HttpResponse
from .models import leaderBoard
from django.shortcuts import render


def index(request):
    if request.method == 'POST':
        teamFirst = request.POST.get('firstTeam')
        teamSecond = request.POST.get('secondTeam')
        scoreFirst = (int(request.POST.get('firstScore')))
        scoreSecond = (int(request.POST.get('secondScore')))
        can = leaderBoard.objects.filter(teamName=teamFirst).exists()
        a = leaderBoard(teamName=teamFirst)
        if can:
            a = leaderBoard.objects.get(teamName=teamFirst)
        b = leaderBoard(teamName=teamSecond)
        can = leaderBoard.objects.filter(teamName=teamSecond).exists()
        if can:
            b = leaderBoard.objects.get(teamName=teamSecond)
        a.goals_for = a.goals_for + scoreFirst
        b.goals_for = b.goals_for + scoreSecond
        a.goals_against = a.goals_against + scoreSecond
        b.goals_against = b.goals_against + scoreFirst
        a.goals_difference = a.goals_for - a.goals_against
        b.goals_difference = b.goals_for - b.goals_against
        a.games_played += 1
        b.games_played += 1
        if scoreFirst == scoreSecond:
            a.draws += 1
            b.draws += 1
            a.points += 2
            b.points += 2
        elif scoreFirst > scoreSecond:
            a.wins += 1
            b.loss += 1
            a.points += 4
            b.points -= 1
        else:
            b.wins += 1
            a.loss += 1
            b.points += 4
            a.points -= 1
        a.save()
        b.save()
        table = leaderBoard.objects.all().order_by('-points', '-goals_difference')
        context = {
            'table': table,
        }
        return render(request, 'leaderboard/index.html', context)
    else:
        table = leaderBoard.objects.all().order_by('-points', '-goals_difference')
        context = {
            'table': table,
        }
        return render(request, 'leaderboard/index.html', context)


# def index(request):
#     table = leaderBoard.objects.all()
#     html = ''
#     for team in table:
#         html += '<p1>' + team.teamName + ' ' + str(team.wins) + ' ' + str(team.games_played) + '</p1><br>'
#     return HttpResponse(html)
def delete(request):
    # leaderBoard.objects.get(id=1).delete()
    table = leaderBoard.objects.all()
    table.delete()
    context = {
        'table': table,
    }
    return render(request, 'leaderboard/deleted.html', context)
