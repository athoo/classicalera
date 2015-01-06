<!DOCTYPE html>
<html lang="en">

<head>

    <meta charset="utf-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <meta name="description" content="">
    <meta name="author" content="">

    <title>白話-文言 翻譯助手</title>

    <!-- Bootstrap Core CSS -->
    <link href="/static/css/bootstrap.min.css" rel="stylesheet">
    <link href="/static/css/about.css" rel="stylesheet">

    <!-- jQuery Version 1.11.1 -->
    <script src="/static/js/jquery.js"></script>
    <script type='text/javascript' src='http://ajax.googleapis.com/ajax/libs/jquery/1.3.2/jquery.min.js?ver=1.3.2'></script>
    <script type='text/javascript' src='/static/js/jquery.mousewheel.min.js'></script>

    <!-- Bootstrap Core JavaScript -->
    <script src="/static/js/bootstrap.min.js"></script>
    <script type="text/javascript" charset="utf-8" src="/static/js/jquery.tubular.1.0.js"></script>
    <script type="text/javascript" charset="utf-8" src="/static/js/index.js"></script>

    <!-- HTML5 Shim and Respond.js IE8 support of HTML5 elements and media queries -->
    <!-- WARNING: Respond.js doesn't work if you view the page via file:// -->
    <!--[if lt IE 9]>
        <script src="https://oss.maxcdn.com/libs/html5shiv/3.7.0/html5shiv.js"></script>
        <script src="https://oss.maxcdn.com/libs/respond.js/1.4.2/respond.min.js"></script>
    <![endif]-->

</head>

<body>

    <!--<img class="img-set" id="img-1" src="static/bg_map.jpg">-->
    <!--<img class="img-set" id="img-2" src="static/2.png">-->
    <!--<img class="img-set" id="img-3" src="static/3.png">-->
    <!--<img class="img-set" id="img-4" src="static/4.png">-->
    <!--<img class="img-set" id="img-5" src="static/5.png">-->
    <!--<img class="img-set" id="img-6" src="static/6.png">-->
    <!--<img class="img-set" id="img-7" src="static/7.png">-->


    <!-- Navigation -->
    <nav class="navbar navbar-inverse navbar-fixed-top" role="navigation">
        <div class="container">
            <!-- Brand and toggle get grouped for better mobile display -->
            <div class="navbar-header">
                <button type="button" class="navbar-toggle" data-toggle="collapse" data-target="#bs-example-navbar-collapse-1">
                    <span class="sr-only">Toggle navigation</span>
                    <span class="icon-bar"></span>
                    <span class="icon-bar"></span>
                    <span class="icon-bar"></span>
                </button>
                <a class="navbar-brand" href="/">Classical Era</a>
            </div>
            <!-- Collect the nav links, forms, and other content for toggling -->
            <div class="collapse navbar-collapse" id="bs-example-navbar-collapse-1">
                <ul class="nav navbar-nav">
                    <li>
                        <a href="/about">About</a>
                    </li>
                    <li>
                        <a href="#">Services</a>
                    </li>
                    <li>
                        <a href="#">Contact</a>
                    </li>
                </ul>
            </div>
            <!-- /.navbar-collapse -->
        </div>
        <!-- /.container -->
    </nav>


    <!-- Page Content -->
    <div class="container" id="main">

        <div id="title" class="row">
            <div class="col-lg-12 text-center">

{% filter markdown %}
# 文言文—白話文 對譯問題

## Problem

## System Design

1.collect raw material
2.build parallel corpus
3.word segmentation
4.language model
5.api service
6.web application


## raw material

![Imgur](http://i.imgur.com/6bIIfgw.png)

- 古文觀止全文（除春秋時期作品、四六文）

- Parse the parallel corpus from the web.
    - crawl with beautifulsoup


## Statistical Machine Translation - Moses

![Imgur](http://i.imgur.com/jAKdX2b.png)


## Data Preparation

Parallel Corpus
  - separate the raw data according to the punctuation
  - using python module Zhon
- Word Segmentation
  - Jieba - A open source python library for Chinese segmentation
  - human- Adding dictionary(human name etc.) for better segmentation
- Build Language Model with IRSLM
- Build Translation Model with Moses

## Backend Server

- Moses provides a server interface, but is based on XMLRPC. (out of date)

![Imgur](http://i.imgur.com/Q5ieanQ.png)

- Write a little server wrapper with Flask to provide REST API.
- A heroku hosted web application



{% endfilter %}
<br>
<br>




            </div>
        </div>
        <!-- /.row -->

    </div>





    <div class="footer">
      <!--<div class="container">-->
        <!--<div class="row">-->
          <div class="col-md-6">
            <ul class="list-inline">
              <li>source</li>
              <li>example</li>
              <li>made by Tsing Hua</li>
            </ul>
          </div>
    </div>

</body>

</html>
