#!/usr/bin/env python

import json
import sys

sections_names = ["section*", "subsection*", "subsubsection*"]

def escape(f):
    return f.replace("\n", "\\\\").replace("^", "\\^{}").replace("#", "\\#").replace("%", "\\%")


def handle_children(js, level):
    for s in js["sections"]:
        if "type" not in s:
            s["type"] = "None"

        if s["type"] == "employment":
            print("\\end{multicols}")

        if "name" in s:
            print("\\" + escape(sections_names[level]) + "{" + s["name"] + "}")

        if len(s["type"]) > 6 and s["type"][:6] == "result":
            print("\\textit{"+s["when"]+", "+s["where"]+"}")


        if s["type"] == "column_break":
            print("\\vfill\\null\n\\columnbreak")
        elif s["type"] == "h_rule":
            print("\\end{multicols}")
            print("\\rule{\\textwidth}{1pt}")
            print("\\begin{multicols}{2}")
        elif s["type"]=="text":
            print(s["data"])
        elif s["type"] == "employment":
            print("\\begin{multicols*}{2}")
            for d in s["data"]:
                print("\\textbf{"+d["when"]+"}")
                print(d["name"]+", "+d["where"]+". "+d["more"]+"\\par")
            print("\\end{multicols*}")
            print("\\begin{multicols}{2}")
        elif s["type"] == "results_vtable":
            print("\\vspace{1em}\\par\\begin{center}\\begin{tabular}{ "+"c "*s["cols"]+"}")
            q = 0
            for f in s["data"]:
                q+=1
                t ="\\makecell{"+escape(f)+"\\vspace{0.5em}}"
                if q == s["cols"]:
                    q=0
                    print(t+"\\\\")
                else:
                    print(t+"&")
            if q!=0:
                print("& "*(s["cols"]-q-1)+" \\\\")
            print("\\end{tabular}\\end{center}")
        elif s["type"] == "results_htable":
            print("\\vspace{1em}\\par\\begin{center}\\begin{tabular}{ "+"c "*s["cols"]+"}")
            q = 0
            r_1 = ""
            r_2 = ""
            for _s,_g in s["data"].items():
                q+=1
                a ="\\makecell{\\textbf{"+escape(_s)+"}}"
                b ="\\makecell{"+escape(_g)+"\\vspace{0.5em}}"
                if q == s["cols"]:
                    q=0
                    r_1+=a+"\\\\"
                    r_2+=b+"\\\\"
                    print(r_1)
                    print(r_2)
                    r_1=""
                    r_2=""
                else:
                    r_1+=a+"& "
                    r_2+=b+"& "
            if q!=0:
                r_1+="& "*(s["cols"]-q-1)+" \\\\"
                r_2+="& "*(s["cols"]-q-1)+" \\\\"
                print(r_1)
                print(r_2)
                r_1=""
                r_2=""
            print("\\end{tabular}\\end{center}")
        elif s["type"] == "list":
            print("\\begin{itemize}")
            for v in s["data"]:
                print("\\item")
                if "head" in v:
                    print("\\textbf{"+escape(v["head"])+":} ")
                if "data" in v:
                    print(escape(v["data"]))
                if "url" in v:
                    print("\\url{"+escape(v["url"])+"}")
            print("\\end{itemize}")
        else:
            #print(s["type"])
            pass
        if "sections" in s:
            handle_children(s, level + 1)


js = None
exe, path = sys.argv
with open(path, "r") as file:
    js = json.loads(file.read())

print(
    """\\documentclass{article}
\\usepackage[utf8]{inputenc}
\\usepackage{auto-pst-pdf}
\\usepackage{fontenc,unicode-math}
\setmainfont[Ligatures=TeX]{TeX Gyre Adventor}

\\usepackage{multicol}
\\usepackage{makecell}
\\usepackage{geometry}
\\usepackage{url}
\\geometry{a4paper, portrait, margin=1.5cm}

\\begin{document}
"""
)
print("\\begin{center}")
print("\\textbf{\\LARGE "+js["name"] + "}\\\\")
print(js["email"])
print("\\end{center}")
print(js["desc"])
print("\\begin{multicols}{2}")
handle_children(js, 0)
print("\\end{multicols}")
print("\\end{document}")
