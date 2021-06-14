from django.shortcuts import render

from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import BoardSerializer
from rest_framework import status
from .models import MyBoard

app_name = "rest_api_board"


class BoardView(APIView):
    """
    GET /boards/
        /boards/{id}
    """
    def get(self, req, **kwargs):
        boardId = kwargs.get('idx')
        if boardId is None:
            boardQueryset = MyBoard.objects.all()
            boardQuerysetSerializer = BoardSerializer(boardQueryset, many=True)
            return Response(boardQuerysetSerializer.data, status=status.HTTP_200_OK)
        else:
            boardSrializer = BoardSerializer(MyBoard.objects.get(id=boardId))
            return Response(boardSrializer.data, status=status.HTTP_200_OK)
    """
    PUT / boards / {id}    
    """

    def put(self, req, **kwargs):
        boardId = kwargs.get('idx')
        if boardId is None:
            return Response("invalid request", status=status.HTTP_400_BAD_REQUEST)
        else:
            boardObj = MyBoard.objects.get(id=boardId)

            updateBoardSerializer = BoardSerializer(boardObj, data=req.data)
            if updateBoardSerializer.is_valid():
                updateBoardSerializer.save()
                return Response(updateBoardSerializer.data, status=status.HTTP_200_OK)
            else:
                return Response(updateBoardSerializer.errors, status=status.HTTP_400_BAD_REQUEST)

    """
    POST / boards / {id}    
    """
    def post(self,req):
        board_serializer = BoardSerializer(data=req.data)
        if board_serializer.is_valid():
            board_serializer.save()
            return Response(board_serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(board_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    """
    DELETE / boards / {id}    
    """
    def delete(self, req, **kwargs):
        boardId = kwargs.get('idx')
        if boardId is None:
            return Response("invalid request", status=status.HTTP_400_BAD_REQUEST)
        else:
            boardObj = MyBoard.objects.get(id=boardId)
            boardObj.delete()
            return Response("delete OK", status=status.HTTP_200_OK)


