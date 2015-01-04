#!/usr/bin/env python
# -*- coding: utf-8 -*-

# enable debugging
import cgitb
cgitb.enable()

print "Content-Type: text/html;charset=utf-8"
print
print """ <script type="text/x-mathjax-config">
  MathJax.Hub.Config({
    extensions: ["tex2jax.js"],
    jax: ["input/TeX", "output/HTML-CSS"],
    tex2jax: {
      inlineMath: [ ['$','$'], ["\\(","\\)"] ],
      displayMath: [ ['$$','$$'], ["\\[","\\]"] ],
      processEscapes: true
    },
    "HTML-CSS": { availableFonts: ["TeX"] }
  });
</script>
 <script type="text/javascript"
   src="http://cdn.mathjax.org/mathjax/latest/MathJax.js">
</script> """


print "Hello World! <p>"
print "Bonjour ! éhé vive les accents français !<p>"
print "$\\frac{1}{2}$<p>"

print "$\\begin{array}{|cc|}  a & b \\\\  c & c \\end{array}$<p>"

print "$\\begin{equation}   E = mc^2 \\end{equation}$<p>"

print """ In equation \\eqref{eq:sample}, we find the value of an
interesting integral:

$\\begin{equation}
  \\int_0^\\infty \\frac{x^3}{e^x-1}\\,dx = \\frac{\\pi^4}{15}
  \\label{eq:sample}
\\end{equation}$<p>"""

print("<h1> Calculs avec Sympy et affichage avec MathJax ! </h1>")

from sympy import *
x = symbols('x')
affichage = latex(Integral(sqrt(1/x), x))
print('$'+affichage+'$')
print('<p>')
expr=(x+1)**10
expr1=latex(expr)
expr2=latex(expand(expr))
print('$'+expr1+'='+expr2+'$')
