<template>
        <div class="detail_body form-horizontal">
            <div ref="md5Menu" id="md5_menu" class="">
                <p class="ClassHead-wrap">
                    <a ref="md5" href="javascript:void(0)" class="m_active" @click="check('md5')" value="md5">MD5加/解密</a>
                    <a ref="b64" href="javascript:void(0)" class="n_active" @click="check('b64')" value="b64">Base64加/解密</a>
                    <a ref="hash" href="javascript:void(0)" class="n_active" @click="check('hash')" value="hash">Hash加/解密</a>
                </p>
            </div>
            <div class="form-group" id="keyValue">
                <div class="col-sm-6">
                    <textarea ref="key" id="key" placeholder="请输入需要加密的内容" v-model="key"></textarea>
                </div>
                <div class="col-sm-6">
                    <textarea ref="val" id="md5" placeholder="请输入需要解密的内容" v-model="val"></textarea>
                </div>
            </div>
            <div class="text-center">
                <button id="getValue" @click="getValue()">加密</button>
                <button id="getKey" @click="getkey()">解密</button>
            </div>
        </div>
</template>
<script>
export default {
    data(){
        return{
            isCheck:0,
            key:'',
            val:'',
        }
    },
    methods:{
        check(val) {
            this.$refs.key.value="";
            this.$refs.val.value="";
            let pNodes = this.$refs;
            let v='';
            for (v in pNodes){
                if(pNodes[v].tagName=="A"){
                    if(v != val){
                        pNodes[v].className = 'n_active';
                    }else{
                        pNodes[v].className = 'm_active';
                    }
                }
            }
        },
        getValue() {
                let {key}=this
                if(key == ''){
                    alert("请输入被加密内容...");
                }else {
                    let md5 = this.$refs.md5Menu.getElementsByClassName("m_active")[0].getAttribute("value");
                    //let ajax = new XMLHttpRequest();
                    let that = this;
                    $.ajax(
                            {
                                type:"get",
                                url:"api/md5/",
                                data:{
                                        "key":key,
                                        "type":md5,
                                        "action":"getValue"
                                },
                                success:function (data) {
                                    //let p = "<textarea rows='4' cols='50'>"+data+"</textarea>";
                                    that.val="";
                                    that.val=data;
                                },
                                error:function () {
                                    alert("error");
                                }
                            }
                    );
                }
            },
        getkey() {
                let md5 = this.$refs.md5Menu.getElementsByClassName("m_active")[0].getAttribute("value");
                if(md5 != "b64") {
                    alert("目前只支持base64解密！");
                }else{
                    let key = this.val;
                    if(key == ''){
                        alert("请输入被解密内容...");
                    }else {
                        let that = this;
                        $.ajax(
                                {
                                    type:"get",
                                    url:"api/md5/",
                                    data:{
                                            "key":key,
                                            "type":md5,
                                            "action":"getKey"
                                    },
                                    success:function (data) {
                                        //let p = "<textarea rows='4' cols='50'>"+data+"</textarea>";
                                        that.$refs.key.value="";
                                        that.$refs.key.value=JSON.stringify(JSON.parse(data), null, 2);
                                        //$("#key").val(JSON.stringify(JSON.parse(data), null, 2));
                                    },
                                    error:function () {
                                        alert("error");
                                    }
                                }
                        );
                    }
                }
            }
    }
}
</script>
<style scoped>
        #md5_menu{
            height: 50px;
            width: 100%;
            font-size: 14px;
            text-align: center;
            margin-top: 7px;
        }
        #key {
            float: left;
            resize: none;
            height: 200px;
            width: 100%;
        }
        #md5 {
            float: right;
            resize: none;
            height: 200px;
            width: 100%;
        }
        #keyValue{
            height: 200px;
        }
        .m_active{
            padding: 0px 25px;
            line-height: 33px;
            height: 33px;
            color: #56688a;
            text-decoration: none;
            border: 1px solid #c6cede;
            /* border-top: 2px #56688a; */
            border-bottom: 2px solid #fff;
        }
        .n_active{
            display: inline-block;
            padding: 0px 20px;
            line-height: 33px;
            height: 33px;
            cursor: pointer;
            color: #0474c8;
            border-width: 2px 1px 0px 1px;
            border-color: #fff;
            border-style: solid;
            /* border-bottom: 1px solid #c6cede; */
        }
        .ClassHead-wrap{
            /*width: 1200px;*/
            margin: 0px auto;
            background: #fff;
            height: 36px;
            _height: 37px;
            padding-top: 10px;
            background: url("../../static/images/nBarbg.png") #fff left bottom repeat-x;
        }
</style>