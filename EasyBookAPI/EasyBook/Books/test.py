from django.http import JsonResponse

from .models import Book, BooksReadByUser


def cancer(request):
    # book = Book.objects.all()
    # print(book)

    mierdon = BooksReadByUser.objects.all()
    print(mierdon)
    BooksReadByUser.objects.all().delete()
    # mierda.delete()


    return JsonResponse({'puta': 'mierda'}, safe=False)




