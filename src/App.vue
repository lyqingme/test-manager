<template>
  <div id="app">
    <h1 class="title">测试小助手</h1>
    <!-- <div id="nav">
     <router-link :to="{ name: 'home' }">Vue</router-link> |
     <router-link :to="{ name: 'messages' }">Django Rest</router-link>
    </div>
    <router-view/> -->
    <div class="panel panel-default main-left">
        <div class="panel-body">
            <ul class="treeview">
                <li>
                    <a href="{% url 'home' %}">首页</a>
                    <!-- {% comment %}<span class="icon glyphicon glyphicon-chevron-left"></span>
                    <ul>
                        <li><a href="#">深度加密1</a></li>
                        <li><a href="#">深度加密2</a></li>
                        <li><a href="#">深度加密3</a></li>
                    </ul>{% endcomment %} -->
                </li>
                <li>
                    <a href="{% url 'md5' %}">md5加密</a>
                    <!-- glyphicon glyphicon-chevron-down -->
                    <!--<span class="icon glyphicon glyphicon-chevron-left"></span>
                    <ul>
                        <li>
                            <a href="#">加密</a>
                            <span class="icon glyphicon glyphicon-chevron-left"></span>
                            <ul>
                                <li><a href="#">深度加密1</a></li>
                                <li><a href="#">深度加密2</a></li>
                                <li><a href="#">深度加密3</a></li>
                            </ul>
                        </li>
                    </ul> -->
                </li>
                <li><a href="{% url 'json' %}">json格式化</a></li>
                <li><a href="{% url 'redis' %}">redis查询</a></li>
                <li><a href="{% url 'hbase' %}">hbase查询</a></li>
                <li><a href="{% url 'mysql' %}">mysql查询</a></li>
                <li><a href="{% url 'xget' %}">http请求（get）</a></li>
<!-- {#                <li><a href="{% url 'bsautest' %}">大屏实时自动化测试</a></li>#}
                <li><a href="{% url 'treasury' %}">treasury自动化打包</a></li>
{#                <li><a href="{% url 'jmx' %}">jmx</a></li>#}
{#                <li><a href="{% url 'host' %}">host切换</a></li>#} -->
            </ul>
        </div>
    </div>
  </div>
</template>

<script>
export default {
  
}
</script>


<style>
/* #app {
  font-family: 'Avenir', Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  margin-top: 60px;
} */
.panel.panel-default {
            float: left;
            overflow: hidden;

             width: 200px;
            height: 625px;
            overflow-x: auto;
            overflow-y: auto;
            border: none;
            box-shadow: none;
            background-color: #30404f;
            margin-bottom: 0;
        }

        div.panel:first-child {
        /* {#margin-top: 20px;#}*/
        } 

        div.treeview {
            min-width: 100px;
            min-height: 100px;

            max-height: 256px;
            overflow: auto;

            padding: 4px;

            margin-bottom: 20px;

            color: #369;

            border: solid 1px;
            border-radius: 4px;
        }

        div.treeview ul:first-child:before {
            display: none;
        }

        .treeview,
        .treeview ul {
            margin: 0;
            padding: 0;
            list-style: none;

            color: #369;
        }

        .treeview ul {
            margin-left: 1em;
            position: relative
        }

        .treeview ul ul {
            margin-left: .5em
        }

        .treeview ul:before {
            content: "";
            display: block;
            width: 0;
            position: absolute;
            top: 0;
            left: 0;
            border-left: 1px solid;
            bottom: 15px;
        }

        .treeview li {
            margin: 0;
            padding: 0 1em;
            line-height: 2em;
            font-weight: 700;
            position: relative
        }

        .treeview ul li:before {
            content: "";
            display: block;
            width: 10px;
            height: 0;
            border-top: 1px solid;
            margin-top: 1px;
            position: absolute;
            top: 1em;
            left: 0
        }

        .tree-indicator {
            margin-right: 5px;

            cursor: pointer;
        }

        .treeview li a {
            text-decoration: none;
            color: inherit;

            cursor: pointer;
        }

        .treeview li button,
        .treeview li button:active,
        .treeview li button:focus {
            text-decoration: none;
            color: inherit;
            border: none;
            background: transparent;
            margin: 0px 0px 0px 0px;
            padding: 0px 0px 0px 0px;
            outline: 0;
        }

        ul {
        /* {#background-color: transparent;#} */
            background-color: #30404f;
        }

        ul li {
            color: #a2b1c4;
             background-color: #2f4050;
        }

        ul li.active {
            color: #fffef8;
            background-color: #2a3845;
        }

        ul li:hover {
            background-color: #455a64;
            color: white;
        }

        /* {#.panel {#}
        {#    width: 200px;#}
        {#    height: 625px;#}
        {#    overflow-x: auto;#}
        {#    overflow-y: auto;#}
        {#    border: none;#}
        {#    box-shadow: none;#}
        {#    background-color: #30404f;#}
        {#    margin-bottom: 0;#}
        {#}#} */

        .form-group {

        }
        .hbase{}
        .main-left{
            position: absolute;
            top: 0;
            left: 0;
        }



.clearfix:after, .clearfix:before, .container-fluid:after, .container-fluid:before,
.container:after, .container:before, .dl-horizontal dd:after, .dl-horizontal dd:before,
.form-horizontal .form-group:after, .form-horizontal .form-group:before,
.modal-footer:after, .modal-footer:before, .modal-header:after,
.modal-header:before, .nav:after, .nav:before, .navbar-collapse:after,
.navbar-collapse:before, .navbar-header:after, .navbar-header:before,
.navbar:after, .navbar:before, .pager:after, .pager:before, .panel-body:after, .panel-body:before, .row:after, .row:before{display: inline-block}

.col-sm-9.xget{float: none;margin-top: 20px;}
  /*   {#    json页面#} */
        .json{
            height: 217px;}
</style>
