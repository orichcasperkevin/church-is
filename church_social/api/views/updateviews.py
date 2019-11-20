from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from church_social.models import DiscussionContribution,CommentToContribution

class VoteContribution(APIView):
    '''
        patch:
        upvote a discussion contribution
    '''
    def patch(self, request ,contribution_id):
        try:
            up = request.data.get("up")
            contribution = DiscussionContribution.objects.get(id=contribution_id)
            up_votes = contribution.votes_up
            down_votes = contribution.votes_down

            if (up):
                contribution.votes_up = up_votes + 1
            else:
                contribution.votes_down = down_votes + 1

            contribution.save()
            return Response(status=status.HTTP_204_NO_CONTENT)

        except:
            return Response(status=status.HTTP_400_BAD_REQUEST)

class VoteComment(APIView):
    '''
        patch:
        upvote a comment.
    '''
    def patch(self, request ,comment_id):
        try:
            up = request.data.get("up")
            comment = CommentToContribution.objects.get(id=comment_id)
            up_votes = comment.votes_up
            down_votes = comment.votes_down

            if (up):
                comment.votes_up = up_votes + 1
            else:
                comment.votes_down = down_votes + 1

            comment.save()
            return Response(status=status.HTTP_204_NO_CONTENT)

        except:
            return Response(status=status.HTTP_400_BAD_REQUEST)
