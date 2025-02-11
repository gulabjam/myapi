from fastapi import FastAPI
from typing import Dict, List
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI ()

student_marks = [{"name":"84b","marks":3},{"name":"ouO6EVs7","marks":96},{"name":"PBuGIO6Fg","marks":16},{"name":"Jse7","marks":84},{"name":"tLbiGgA","marks":75},{"name":"tMT0ZND","marks":71},{"name":"iPuXrqq","marks":12},{"name":"cne","marks":54},{"name":"V4h","marks":29},{"name":"AYcog1l","marks":27},{"name":"p4CkWC1Qvb","marks":25},{"name":"cHIV","marks":95},{"name":"Ww54wejwC","marks":64},{"name":"wReVFF7P","marks":11},{"name":"HH6","marks":71},{"name":"OkeHy8io","marks":49},{"name":"fV","marks":8},{"name":"0e","marks":0},{"name":"o1svPti","marks":78},{"name":"cTkUi","marks":20},{"name":"JtzRw","marks":28},{"name":"8mBLvsh1bl","marks":70},{"name":"3v","marks":48},{"name":"x","marks":18},{"name":"mfLM4D","marks":61},{"name":"zH","marks":26},{"name":"mH","marks":90},{"name":"7EZdk5uH","marks":65},{"name":"9WG54167","marks":88},{"name":"Cx","marks":13},{"name":"N8gwEShk2h","marks":67},{"name":"4d6hP","marks":21},{"name":"AwOht2V","marks":38},{"name":"Dmz7OhS6O","marks":35},{"name":"N7SOrExPuV","marks":94},{"name":"cS","marks":92},{"name":"hZn4","marks":22},{"name":"x5goQf7j15","marks":20},{"name":"lQ0qKA","marks":73},{"name":"ecIGzXLwkr","marks":26},{"name":"Q6aV2MIXXS","marks":72},{"name":"zn","marks":24},{"name":"w6","marks":95},{"name":"IvN8bo","marks":15},{"name":"5zoWoKcO3","marks":89},{"name":"B","marks":70},{"name":"H2rrm4","marks":8},{"name":"rvS5I0","marks":61},{"name":"lrZjx8B","marks":83},{"name":"KQA5qpsSZG","marks":19},{"name":"6Bu71T","marks":17},{"name":"NFyupLLJOl","marks":30},{"name":"1eRrxD","marks":45},{"name":"ScwAyqpS","marks":19},{"name":"xBjWrRNU","marks":91},{"name":"U","marks":15},{"name":"iGO","marks":5},{"name":"Kl","marks":42},{"name":"7","marks":20},{"name":"V","marks":9},{"name":"TJHx1v","marks":92},{"name":"MUWiqONeM","marks":22},{"name":"Gm3GYhRDmv","marks":47},{"name":"vZCJ","marks":88},{"name":"XIC","marks":72},{"name":"jSwGO","marks":15},{"name":"qn2","marks":70},{"name":"Xx6vNxJiL","marks":13},{"name":"1Z6OKPE","marks":4},{"name":"U","marks":91},{"name":"nh6uoRC","marks":22},{"name":"mm0hHy","marks":3},{"name":"E","marks":73},{"name":"2Ljnri37G","marks":18},{"name":"c7hvRI","marks":73},{"name":"v","marks":90},{"name":"eB3MlQa","marks":61},{"name":"y8","marks":14},{"name":"l","marks":97},{"name":"fh8ihU4n","marks":59},{"name":"P","marks":53},{"name":"BPCY","marks":72},{"name":"8F","marks":39},{"name":"2TB1cLeJT","marks":16},{"name":"p","marks":92},{"name":"MFZo","marks":26},{"name":"0Ep7Ev3","marks":62},{"name":"OzThrO","marks":70},{"name":"Qtj","marks":75},{"name":"sjQFSW3Br","marks":11},{"name":"PBagQxbt","marks":25},{"name":"9XyqmMy","marks":66},{"name":"mgl5KltI","marks":80},{"name":"iBPQ3TkRH5","marks":13},{"name":"pvRFhXZ","marks":74},{"name":"4d","marks":57},{"name":"Uqi","marks":48},{"name":"duNY","marks":98},{"name":"eKbh1PW","marks":98},{"name":"9Mdt","marks":14}]
app.add_middleware(CORSMiddleware, allow_origins=["*"]) 

@app.get("/api")
def get_marks (name1 : str, name2 : str):
    list = []
    list2 = {name1, name2}
    for i in list2:
        for j in student_marks:
            if j["name"] == i:
                list.append(j["marks"])
                break
    return {"marks" : list}
