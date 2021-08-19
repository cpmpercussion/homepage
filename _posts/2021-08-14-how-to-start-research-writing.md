---
layout: post
title:  How to get started with research writing
date:   2021-08-14 20:00:00 +1000
---

Now's the time of year that I get started with a new crop of Honours, Master and project students at the [ANU School of Computing](https://cs.anu.edu.au) and at the [UiO Department of Informatics](https://ifi.uio.no).

All of my CS project students produce a report or thesis for their assessment. This will be the most important part of the assessment for your project and you'll probably put quite a bit of effort into writing it.

In this post I'll set down some of the most important advice I give students when getting stated.

## Structure

Is there a default structure for a thesis or report or should everybody write whatever they want? Although there usually aren't **rules** about structuring a thesis, it's usually a good idea to follow the usual **conventions** for academic writing which is often summed up as ILMRaD:

1. Introduction
2. Literature Review
3. Methods
4. Results
5. (and) Discussion 
6. (and conclusion)

The idea is that you have these words as the titles for the five-six chapters in your thesis. Pat Thomson writes about it more [here](https://patthomson.net/2012/10/19/is-there-a-format-for-a-thesis/).

There are some field-specific chapter titles that you might also use. For instance, in computing where we build a new system and experiment with it, we often use a "System Design" chapter instead of "Methods" and you might discuss your experimental method at the start of the results section. The Conclusion is often it's own chapter at the end.

I suggest that most students use this convention. Why? Because it helps examiners to find the information they need quickly and helps you to make sure you provide the information that they typically look for.

## Formatting

Most computer science and music tech papers and theses are formatted using LaTeX (not Microsoft Word). With LaTeX you edit a plain text document with markup to indicate formatting rather than what-you-see-is-what-you-get environments like Word. LaTeX is particularly good at displaying **maths** and handling **references** (with Bibtex). Overall many academic folks prefer the quality of the output document which seems a lot more polished than Word.

You can get a TeX environment for your system which will include the software to compile e.g., MacTex for macOS, TeXLive for Linux.

You can also use cloud-based editors like [Overleaf](https://www.overleaf.com/).

A similar option is to write in Markdown and use [Pandoc]() to convert to a pdf (via LaTeX).

## Length

Length for a thesis or report can vary, but here are some guidelines for the _maximum_ length of a LaTeX-generated PDF file for project courses of different sizes (in ANU course units where 48 units is 1-year full time).

- 30 pages for 6-unit projects, 
- 50 pages for 12 units, 
- 70 pages for 18 units, 
- 90 pages for 24 units

(BTW these are borrowed from our Engineering project courses! thx folks!)

LaTeX generated theses tend to be a bit longer than a Word document because they add a bit more white space etc. Computing and engineering works often have lots of figures and images so the length can look extremely long for some people. In fact, many students end up blowing these page budgets and have to reduce the size of their work afterwards.

## References


## Introduction and Conclusion

Here's some specific advice for your intro and conclusion.

## Introduction:

Your introduction needs to explain:

- What is your problem?
- Why is it interesting?
- What have you done to solve it?  (What are your aims/research questions?)
- What were the results?

Basically a mini version of the whole thesis! 

Need to focus on the problem, and the "why" of your project. 

Important to set up the aims and research questions of the project clearly and to briefly state the main results so the reader knows what to expect and so that you can address them in more detail in the conclusion.

## Conclusion:

Similar to your introduction!

This time, focus on what you accomplished, addressing the aims/RQs with the findings.

Also need to put your thesis into context a bit — this is where “future work” fits, but also writing about how your work could be applied and what it MEANS in the world outside of this project.

## Both parts

- Both intro and conclusion need to have the basic information of your thesis
- Intro is more focussed on setting up the problem, the why, and you aims
- Conclusion more focussed on address the aims using evidence from your findings.
- Conclusion also puts work into context.

## Some online resources:

- Abstract: <https://patthomson.net/2013/12/11/writing-the-thesis-abstract/>
- Introduction: <https://patthomson.net/2014/06/02/the-thesis-introduction/>
- Conclusion: <https://patthomson.net/2012/12/19/conclusion-mise-en-place-christmas-present-six/>
- More: <https://thesiswhisperer.com>