---
layout: post
title: Posterous exporter for Toto
categories:
- Note
tags:
- Toto
- Script
- Ruby
- code
- Posterous
status: publish
type: post
published: true
meta: {}
---

I’ve been experimenting a bit with a cute blogging engine called 
[Toto](http://cloudhead.io/toto) and wanted to migrate my Posterous posts so I wrote a little script in Ruby to download them all and format them in a Toto-appropriate way.

This script uses the posterous gem just to retrieve each post and put it in a YAML text file that Toto can understand. At the moment there are a few problems…

* Since YAML uses “:” as a control character I had to remove any colons from titles and replaced them with dashes… I wonder if there’s a way to preserve them so that the text files are still human-readable?
* The posterous gem only seems to get one page of posts at a time since my blog has 19 pages, I just ran my downloading method for each one.

Anyway, here’s the script! Maybe someone will chime in and tell me all the things I’m doing wrong:

    #!/usr/bin/env ruby

    require 'posterous'
    require 'toto'

    Posterous.config = {
      'username'  => 'username',
      'password'  => 'password',
      'api_token' => 'api_token'
    }

    include Posterous

    @site = Site.primary

    Dir.chdir( "~/src/posterousparser" )

    def saveposts(pagenumber = 0)
      @site.posts(:page => pagenumber).each do |e|
        timestamp = e.display_date
        yyyy = timestamp[0..3]
        mm = timestamp[5..6]
        dd = timestamp[8..9]

        title = e.title.gsub(":", "-")
        slug = title.strip.slugize
        filename = "#{yyyy}-#{mm}-#{dd}-#{slug}.txt"

        puts "Writing #{filename}...\n"

        file = File.new("#{filename}", "w")
        file.puts "---\n"
        file.puts "title: #{title}\n"
        file.puts "author: #{e.user["display_name"]}"
        file.puts "date: #{dd}/#{mm}/#{yyyy}\n"
        file.puts "timestamp: #{e.display_date}\n"

        file.print "tags: "

        e.tags.each do |a|
          file.print "#{a["name"]} "
        end

        file.puts "\n\n"
        file.puts "#{e.body_full}\n"
        file.puts "\n"
        file.close

      end
    end

    puts "Downloading posts now!"

    for i in 1..19 do
      saveposts(i)
    end