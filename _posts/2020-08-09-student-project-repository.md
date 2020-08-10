---
layout: post
title:  How to present a student software project
date:   2020-08-09 23:33:59 +1000
---

So you're a student working on an individual project this semester (how exciting!) and your supervisor has asked you to submit the _software_ as well as a _report_. So how are you going to present this great work? An email? A zipfile? A USB key?

You might be thinking: "I've done a lot of programming assignments, this should be the same right?" Well, maybe, maybe not. Unlike an assignment, your audience for a software project _doesn't know what your project is about_, so you have to be clear about telling them! Your project might be for a teacher or examiner at first, but you might want to show it to your colleagues, potential employers, or even to wider open source or research communities. These people will want to know what your project is about, might also want to be able to reuse your code, or see how it works.

It's **really** important that your project documents exactly _how to run your code_. Your audience, either an examiner, teacher, or anybody else, will not have time to try every python file to see which is the one that makes your project *go*, and they certainly won't be able to magically know what the dependencies are for your code. To make these things **obvious** you need to write them in your readme file and provide a `requirements.txt` file (or similar) so that others can actually install and run your work!

For a software project to be **excellent**, presentation matters. If I don't know how code works, then it might as well be broken. Here's some tips for getting this right and submitting work that you (and your teachers) can be proud of!

**This is part of a series of posts for my undergraduate and honours project students at the ANU, but it could be useful to other people, even you!**

## Git Repository as Artefact

_Most_ student software projects should probably be presented as a git repository. This gives you a way to keep track of your work over the project, ways to experiment ([with branches](https://www.atlassian.com/git/tutorials/using-branches)) and [roll back](https://www.atlassian.com/git/tutorials/undoing-changes/git-revert) if you make mistakes. Your supervisor and other collaborators or advisers can check in on your work during the project, and, when it's finished, you could publish your project to a public hosting platform such as [GitHub](https://docs.github.com/en/github/importing-your-projects-to-github/adding-an-existing-project-to-github-using-the-command-line) as part of your online portfolio.

Given that you are setting up a git repository, make sure you have a `.gitignore` file [appropriate for your project](https://docs.github.com/en/github/using-git/ignoring-files), so that you don't commit temporary or unnecessary files.

You should also practice [good git hygiene](https://leosaysger.github.io/blog/code/2019/01/10/git-hygiene.html). In particular, don't commit huge binary files (e.g., PDF, zips, media files) in a git repo, and definitely don't store [passwords or API keys in a git repo](https://www.freecodecamp.org/news/how-to-securely-store-api-keys-4ff3ea19ebda/). 

If your project requires large data files, store them elsewhere (e.g., [CloudStor](https://www.aarnet.edu.au/network-and-services/cloud-services/cloudstor) for Australian research and educational institutions.), and write a [script to download them before they are needed](https://stackoverflow.com/questions/7243750/download-file-from-web-in-python-3).

As a bonus, you can access [public Github repos from Google Colab](https://colab.research.google.com/github/googlecolab/colabtools/blob/master/notebooks/colab-github-demo.ipynb) which is a neat way to show off a project to people without having them download it onto their system.

As a second bonus, a nicely set out git repo will look cool in GitLab or GitHub:

![Charles' Keras MDN Layer Repository]({% link assets/blog/2020/keras-mdn-layer-project.png %})

## Project Structure

Most of my students do projects in Python or iPython Notebooks. Although there are many ways to structure a project, by following best-practices you know that your audience can quickly understand your project and might even try to test/use it!

If your project is in Python, it might be best to structure it as module. You might like to follow the ["Structuring your Project" tutorial (Hitchhiker's guide to python)](https://docs.python-guide.org/writing/structure/#sample-repository), or look at an [example project on GitHub](https://github.com/navdeep-G/samplemod). 

If your project was called `project_name`, it might look like this:

```
charles_martin_compxxxx_project_2020/
+-- README.md
+-- LICENSE
+-- setup.py 
+-- requirements.txt
+-- project_name/
|   +-- __init__.py
|   +-- core.py
|   +-- utils.py
+-- tests/
|   +-- tests.py
+-- data/
|   +-- data.csv (perhaps include data if small)
|   +-- README.md (explains how to download data if large)
```

A few notes here:

- The git repository is not named `charles_martin_compxxxx_project_2020` (not `project_name`), so if you share it with a supervisor (who might have many _compxxxx_ students), they can find **your** project.
- Having a main `README.md` is pretty much mandatory (more below)
- Having a license is good practice for any code you make public as it makes it clear who created the project and under what terms it can be used/reused (if at all).
- The `requirements.txt` file is a lightweight way to list a Python module's requirements. You can and should work in a virtual environment so that you can keep track of [what other modules are required to run your code](https://medium.com/python-pandemonium/better-python-dependency-and-package-management-b5d8ea29dff1). A more advanced way to do this would be with [Poetry](https://python-poetry.org).
- `setup.py` might allow others to [install your module, or for you to distribute it](https://stackoverflow.com/questions/1471994/what-is-setup-py). cool!
- If you only need one code file for your project, you could simply name it `project_name.py` and place it in your repo. If you want multiple files as part of a module, you'll need a directory called `project_name`, and (traditionally) [a main file](https://stackoverflow.com/questions/448271/what-is-init-py-for) called `__init__.py`.

If your project is  a collection of iPython Notebooks, you should use directories to make it obvious where the various parts of the project are (e.g., see [this StackOverflow post](https://stackoverflow.com/questions/45723751/how-to-structure-a-python-project-with-ipython-notebooks)):

```
charles_martin_compxxxx_project_2020/
+-- README.md
+-- LICENSE
+-- requirements.txt
+-- notebooks/
|   +-- experiment_1.ipynb
|   +-- experiment_2.ipynb
|   +-- prepare_data.ipynb
|   +-- utils.py
+-- data/
|   +-- data.csv (perhaps include data if small)
|   +-- README.md (explains how to download data if large)
```

The filenames here make it obvious why there are multiple notebook files, and we still have a readme, license, and `requirements.txt` files.

For an example have a look at my [Keras MDN project](https://github.com/cpmpercussion/keras-mdn-layer)

## README.md

The readme is the most important file in your project. Really. If you don't have a readme, nobody will know what your code is for, or how to install or use it.

You might like to follow a [good readme template](https://gist.github.com/PurpleBooth/109311bb0361f32d87a2), and include some of the following sections:

- title
- project overview
- installing
- downloading data
- how to use
- running the tests
- references

A really **nice** readme might have some cool things like _images_ or demo gifs (see this list of [awesome READMEs for inspiration](https://github.com/matiassingers/awesome-readme), but the above things are a good place to start.

## LICENSE

A license sets out the terms under which others can use, modify or share your code. Do you want to allow others to reuse your code in their own projects? Do you want others to use your code, but _only in similarly licensed projects_? Do you want to reserve all rights unless they negotiate with you?

These are tricky questions. Many of my projects are licensed under the very permissive [MIT License](https://choosealicense.com/licenses/mit/), but this is an individual choice you should make for your own work.

Luckily there's a whole website to help you [choose a license](https://choosealicense.com).

BTW, you can just **not have a license**, which basically means your code is available to view but you retain [exclusive copyright](https://choosealicense.com/no-permission/) over the work. If somebody else wants to use, modify, or share your code, they would need to ask for your permission to do so.

## Status Badges

Oh you like my status badges? You want your repo to say <img src="https://travis-ci.org/dwyl/esta.svg?branch=master" alt="Build Passing" style="width:100px; display:inline-block;vertical-align:middle;" />?

These little badge images appear on lots of nice Git Repos and generally advertise how great and well-tested and published our repos are.

There are [lots of them](https://github.com/badges/shields) available (here's some [instructions](https://github.com/dwyl/repo-badges) on how to find different types).

If your project has tests, you might like to set up [continuous integration](https://docs.github.com/en/actions/building-and-testing-code-with-continuous-integration/setting-up-continuous-integration-using-github-actions) so that anybody who visits **knows it's working** without even trying it.

You can also get a badge for your [license](https://gist.github.com/lukas-h/2a5d00690736b4c3a7ba).

Badges don't mean very much, but they're fun and colourful. Just another way you can show **attention to detail** in your work.

## Videos, Sounds, GIFs, Images

If your project has sound, visuals or an interactive system as the output, then it's probably a good idea to include some documentation of this media in your readme.

GitHub doesn't allow HTML embeds when displaying readme files, but you might make a short (e.g., 10 sec) video into [a gif](https://giphy.com) and include that instead, e.g.:

![](https://media.giphy.com/media/KFoOINQn0moVJB8uUe/giphy.gif)

For sound, you could link to soundfiles stored on [Soundcloud](https://soundcloud.com) or [clyp.it](https://clyp.it), and for video you could link to a YouTube or Vimeo upload.


