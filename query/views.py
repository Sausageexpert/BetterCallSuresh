from django.shortcuts import render
import tkinter
from tkinter import filedialog
from django.http import HttpResponse
'''from .Simpitron import CONSITUTION_EXTRACTION as CE'''

# Create your views here.
def queryView(request):
    return HttpResponse('integrated')
def queryView2(request):
    main = tkinter.Tk()
    main.withdraw()
    filename = filedialog.askopenfilename(initialdir = "/",
                                          title = "Select a File",
                                          filetypes = (("Text files",
                                                        "*.txt*"),
                                                       ("all files",
                                                        "*.*")))
    main.mainloop()
    constitution_path = 'query/requirements/INDIA.txt'
    query_path = filename.initialdir 
    f = open(query_path)
    query = f.read()
    f.close()
    model = CE("INDIA", constitution_path, query)
    answer = model.get_response()
    context = {'answer':answer}
    return render(request, 'query/queryView.html',context)

