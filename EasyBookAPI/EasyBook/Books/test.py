from django.http import JsonResponse

from .models import Book, BooksReadByUser


def testendpoint(request):
    book = Book.objects.all()
    print(book)

    # user = request.user
    # print(user.id)
    # test = BooksReadByUser.objects.all()
    # print(test)


    return JsonResponse({'ay': 'perdon'}, safe=False)




