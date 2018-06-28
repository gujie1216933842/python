var fk;
var mode;
validator={
	errinput : 'errinput',
	errmsg : 'errmsg',
	errcls : 'no',
	yescls : 'yes',

	psd1 : /^[a-zA-Z0-9]{6,16}$/,
	psd2 : /[0-9]{1,}/,
	psd3 : /[a-zA-Z]{1,}/,
//    psd4 : /(([a-zA-Z0-9])\1\1)/,
//    psd5 : /[\w]*(?:(?:0(?=1)|1(?=2)|2(?=3)|3(?=4)|4(?=5)|5(?=6)|6(?=7)|7(?=8)|8(?=9)){3}|(?:9(?=8)|8(?=7)|7(?=6)|6(?=5)|5(?=4)|4(?=3)|3(?=2)|2(?=1)|1(?=0)){3}|(?:A(?=B)|B(?=C)|C(?=D)|D(?=E)|E(?=F)|F(?=G)|G(?=H)|H(?=I)|I(?=J)|J(?=K)|K(?=L)|L(?=M)|M(?=N)|N(?=O)|O(?=P)|P(?=Q)|Q(?=R)|R(?=S)|S(?=T)|T(?=U)|U(?=V)|V(?=W)|W(?=X)|X(?=Y)|Y(?=Z)){3}|(?:a(?=b)|b(?=c)|c(?=d)|d(?=e)|e(?=f)|f(?=g)|g(?=h)|h(?=i)|i(?=j)|j(?=k)|k(?=l)|l(?=m)|m(?=n)|n(?=o)|o(?=p)|p(?=q)|q(?=r)|r(?=s)|s(?=t)|t(?=u)|u(?=v)|v(?=w)|w(?=x)|x(?=y)|y(?=z)){3}|(?:z(?=y)|y(?=x)|x(?=w)|w(?=v)|v(?=u)|u(?=t)|t(?=s)|s(?=r)|r(?=q)|q(?=p)|p(?=o)|o(?=n)|n(?=m)|m(?=l)|l(?=k)|k(?=j)|j(?=i)|i(?=h)|h(?=g)|g(?=f)|f(?=e)|e(?=d)|d(?=c)|c(?=b)|b(?=a)){3}|(?:Z(?=Y)|Y(?=X)|X(?=W)|W(?=V)|V(?=U)|U(?=T)|T(?=S)|S(?=R)|R(?=Q)|Q(?=P)|P(?=O)|O(?=N)|N(?=M)|M(?=L)|L(?=K)|K(?=J)|J(?=I)|I(?=H)|H(?=G)|G(?=F)|F(?=E)|E(?=D)|D(?=C)|C(?=B)|B(?=A)){3})\w/,
	require : /[^(^\s*)|(\s*$)]/,
	email : /^\w+([-+.]\w+)*@\w+([-.]\w+)*\.\w+([-.]\w+)*$/,
	phone : /^((\(\d{2,3}\))|(\d{3}\-))?(\(0\d{2,3}\)|0\d{2,3}-)?[1-9]\d{6,7}(\-\d{1,4})?$/,
	//mobile : /^\d{11}$/,
	mobile : /^0?1(3|4|5|8)\d{9}$/,
	url : /^(http:\/\/|\?)[A-Za-z0-9\-]+[A-Za-z0-9\.\/]+[\/=\?%\-&_~`@[\]\':+!]*([^<>\"\"])*$/,
	url1 : /^(\?)[A-Za-z0-9\-]+[A-Za-z0-9\.\/]+[\/=\?%\-&_~`@[\]\':+!]*([^<>\"\"])*$/,
	url2 : /^(http:\/\/|\?|wapg:\/\/)[A-Za-z0-9\-]+[A-Za-z0-9\.\/]+[\/=\?%\-&_~`@[\]\':+!]*([^<>\"\"])*$/,
    url3:/^((http|https):\/\/|\?)[A-Za-z0-9\-]+[A-Za-z0-9\.\/]+[\/=\?%\-&_~`@[\]\':+!]*([^<>\"\"])*$/,
    url4:/^((http|https):\/\/|\/\?)[A-Za-z0-9\-]+[A-Za-z0-9\.\/]+[\/=\?%\-&_~`@[\]\':+!]*([^<>\"\"])*$/,
    url5:/^(((http|https):\/\/|\/\?)[A-Za-z0-9\-]+[A-Za-z0-9\.\/]+[\/=\?%\-&_~`@[\]\':+!]*([^<>\"\"])*)|(wltgame)(.*?)$/,
	idCard : "this.isIdCard(value)",
	currency : /^\d+(\.\d+)?$/,
	number : /^\d+$/,
    positivenumber:/^(([1-9]\d*(\.[0-9]{1,2})?)|(0\.0[1-9])|(0\.[1-9][0-9]))$/,
	zip : /^[0-9]\d{5}$/,
	ip  : /^[\d\.]{7,15}$/,
	qq : /^[1-9]\d{4,8}$/,
	integer : /^[-\+]?\d+$/,
	double : /^[-\+]?\d+(\.\d+)?$/,
	double1 : /^[-\+]?\d+(\.\d{1,2})?$/,
	double2 : /^\d+(\.\d{1,2})?$/,
	double3 : /^(([1-9]\d*)|(-1){1}|0)$/,
	double4 : /^\d+(\.\d{1,4})?$/,
	english : /^[A-Za-z]+$/,
	chinese : /^[\u0391-\uFFE5]+$/,
	userName : /^[a-z_ ]\w{3,}$/i,
	//unSafe : /^(([A-Z]*|[a-z]*|\d*|[-_\~!@#\$%\^&\*\.\(\)\[\]\{\}<>\?\\\/\'\"]*)|.{0,5})$|\s/,
	unSafe : /[<>\?\#\$\*\&;\\\/\[\]\{\}=\(\)\.\^%,]/,
	//safeStr : /[^#\'\"~\.\*\$&;\\\/\|]/,
	isSafe : function(str){return !this.unSafe.test(str);},
	safeString : "this.isSafe(value)",
	filter : "this.doFilter(value)",
	limit : "this.checkLimit(Common.strlen(value))",
	limitB : "this.checkLimit(this.LenB(value))",
	limitC : "this.checkLimit(this.LenC(value))",
	limitD : "this.checkLimit(this.LenD(value))",
	date : "this.isDate(value)",
	repeat : "this.checkRepeat(value)",
	repeat2 : "this.checkRepeat2(value)",
	range : "this.checkRange(value)",
	compare : "this.checkCompare(value)",
    compareFloat:"this.checkCompareFloat(value)",
	custom : "this.Exec(value)",
	group : "this.mustChecked()",
	ajax: "this.doajax(errindex)",

	isIdCard : function(number){
	var date, Ai;
	var verify = "10x98765432";
	var Wi = [7, 9, 10, 5, 8, 4, 2, 1, 6, 3, 7, 9, 10, 5, 8, 4, 2];
	var area = ['','','','','','','','','','','','北京','天津','河北','山西','内蒙古','','','','','','辽宁','吉林','黑龙江','','','','','','','','上海','江苏','浙江','安微','福建','江西','山东','','','','河南','湖北','湖南','广东','广西','海南','','','','重庆','四川','贵州','云南','西藏','','','','','','','陕西','甘肃','青海','宁夏','新疆','','','','','','台湾','','','','','','','','','','香港','澳门','','','','','','','','','国外'];
	var re = number.match(/^(\d{2})\d{4}(((\d{2})(\d{2})(\d{2})(\d{3}))|((\d{4})(\d{2})(\d{2})(\d{3}[x\d])))$/i);
	if(re == null) return false;
	if(re[1] >= area.length || area[re[1]] == "") return false;
	if(re[2].length == 12){
		Ai = number.substr(0, 17);
		date = [re[9], re[10], re[11]].join("-");
	} else {
		Ai = number.substr(0, 6) + "19" + number.substr(6);
		date = ["19" + re[4], re[5], re[6]].join("-");
	}
	if(!this.isDate(date, "ymd")) return false;
	var sum = 0;
	for(var i = 0;i<=16;i++){
		sum += Ai.charAt(i) * Wi[i];
	}
	Ai += verify.charAt(sum%11);

	return (number.length ==15 || number.length == 18 && number == Ai);
	},

	isDate : function(op){
		var formatString = this['element'].attr('format');
		formatString = formatString || "ymd";
		var m, year, month, day;
		switch(formatString){
		case "ymd" :
			m = op.match(new RegExp("^((\\d{4})|(\\d{2}))([-./])(\\d{1,2})\\4(\\d{1,2})$"));
			if(m == null ) return false;
			day = m[6];
			month = m[5]*1;
			year = (m[2].length == 4) ? m[2] : GetFullYear(parseInt(m[3], 10));
		break;
		case "dmy" :
			m = op.match(new RegExp("^(\\d{1,2})([-./])(\\d{1,2})\\2((\\d{4})|(\\d{2}))$"));
			if(m == null ) return false;
			day = m[1];
			month = m[3]*1;
			year = (m[5].length == 4) ? m[5] : GetFullYear(parseInt(m[6], 10));
		break;
		default :
			break;
		}
		if(!parseInt(month)) return false;
		month = month==0 ?12:month;
		var date = new Date(year, month-1, day);
		return (typeof(date) == "object" && year == date.getFullYear() && month == (date.getMonth()+1) && day == date.getDate());
		function GetFullYear(y){
			return ((y<30 ? "20" : "19") + y)|0;
		}
	}, //end isDate
	doFilter : function(value){
		var filter =this['element'].attr('accept');
		return new RegExp("^.+\.(?=EXT)(EXT)$".replace(/EXT/g,filter.split(/\s*,\s*/).join("|")),"gi").test(value);
	},

	checkLimit:function(len){
		var minval=this['element'].attr('min') ||Number.MIN_VALUE;
		var maxval=this['element'].attr('max') ||Number.MAX_VALUE;
		return (minval<= len && len<=maxval);

	},

	LenB : function(str){
		return $.trim(str).replace(/[^\x00-\xff]/g,"**").length;
	},
	LenC : function(str){
		return $.trim(str).length;
	},
	LenD : function(str){
		m = $.trim(str).match(new RegExp("^([a-zA-Z]|[0-9]|[\u4e00-\u9fa5])+$"));
		if(m == null ) return false;
		return true;
	},
	checkRepeat:function(value){
		var to = this['element'].attr('to');
		return value==jQuery('input[name="'+to+'"]').eq(0).val();
	},

	checkRepeat2:function(value){
		var to = this['element'].attr('to');
		return value==jQuery('#'+to).val();
	},

	checkRange : function(value){
		value = parseFloat(value);
//		value = value|0;
		var minval=this['element'].attr('min') || Number.MIN_VALUE;
		var maxval=this['element'].attr('max') || Number.MAX_VALUE;
		return (minval<=value && value<=maxval);
	},

	checkCompare : function(value){
		if(isNaN(value)) return false;
		value = parseInt(value);
		var operator = this['element'].attr('operator');
		var op1 = value;
		var to = this['element'].attr('to');
		var op2 = this['element'].parent().parent().parent().find('input[name="'+to+'"]').eq(0).val();
		//console.info(op1);
		//console.info(to);
		//console.info(op2);
		switch (operator) {
			case "NotEqual":
			return (op1 != op2);
			case "GreaterThan":
			return (op1 > op2);
			case "GreaterThanEqual":
			return (op1 >= op2);
			case "LessThan":
			return (op1 < op2);
			case "LessThanEqual":
			return (op1 <= op2);
			default:
			return (op1 == op2);
		}
	},
    checkCompareFloat : function(value){
        if(isNaN(value)) return false;
        value = parseFloat(value);
        var operator = this['element'].attr('operator');
        var op1 = value;
        var to = this['element'].attr('to');
        var op2 = this['element'].parent().parent().parent().find('input[name="'+to+'"]').eq(0).val();
        //console.info(op1);
        //console.info(to);
        //console.info(op2);
        switch (operator) {
            case "NotEqual":
                return (op1 != op2);
            case "GreaterThan":
                return (op1 > op2);
            case "GreaterThanEqual":
                return (op1 >= op2);
            case "LessThan":
                return (op1 < op2);
            case "LessThanEqual":
                return (op1 <= op2);
            default:
                return (op1 == op2);
        }
    },
	Exec : function(value){
		var reg = this['element'].attr('regexp');
		return new RegExp(reg,"gi").test(value);
	},

	mustChecked : function(){
		var tagName=this['element'].attr('name');
		var f=this['element'].parents('form');
		var n=f.find('input[name="'+tagName+'"][checked]').length;
		var count = f.find('input[name="'+tagName+'"]').length;
		var minval=this['element'].attr('min') || 1;
		var maxval=this['element'].attr('max') || count;
		return (minval<=n && n<=maxval);
	},

	doajax : function(value) {
		var fk;
		var element = this['element'];
		var errindex = this['errindex'];
		var url=this['element'].attr('url');
		var mode = element.attr('mode') || 1 ;
		var msgid = element.attr('msgid');
		var val = this['element'].val();
		var str_errmsg=this['element'].attr('msg');
		var arr_errmsg = str_errmsg.indexOf('|') ? str_errmsg.split('|') :str_errmsg;
		var errmsg = arr_errmsg[errindex];
		var type=this['element'].attr('type');
		var errcls=this['errcls'];
		var yescls=this['yescls'];
		var param = val ? this['element'].attr('param') + '&value=' + val : this['element'].attr('param');
//		var param = val ? 'value=' + val + '' : '';
		var Charset = $.browser.msie ? document.charset : document.characterSet;
		var methodtype = (Charset.toLowerCase() == 'utf-8') ? 'post' : 'get';
		var method=this['element'].attr('method') || methodtype;
		var s = $.ajax({
			type: method,
			url: url,
			data: param,
			cache: false,
			async: false,
			success: function(data){
				data = data.replace(/(^\s*)|(\s*$)/g, "");
				   if(data != 'success')
				   {
					  errmsg = errmsg ? errmsg : data;
					  fk = false;
					  (type!='checkbox' && type!='radio' && element.addClass('errinput'));
					  if(mode == 1)
					  {
						  if(msgid)
						  {
							  id = '#' + msgid;
							  $(id+'_state').removeClass('bg state_yes').addClass('bg state_no');
							  $(id+'_msg').html(errmsg);
						  }
						  else
						  {
							  jQuery("<span tag='err' class='"+errcls+"'></span>").html(errmsg).insertAfter(element);
						  }

					  }
					  else if(mode == 2)
					  {
						  alert(errmsg);
					  }

					  return false;
				   }
				   else
				   {
					   fk = true;
					   if(msgid)
						{
							id = '#' + msgid;
							$(id+'_state').removeClass('bg state_no').addClass('bg state_yes');
							$(id+'_msg').html('');
						}
						else
						{

							jQuery("<span tag='err' class='"+yescls+"'>&nbsp;</span>").insertAfter(element);
						}
					   return true;
				   }
			   }
		 }).responseText;
		 s = s.replace(/(^\s*)|(\s*$)/g, "");
		 return s == 'success' ? true : false;
	}
};

validator.showErr=function (element, errindex){
	var str_errmsg=element.attr('msg') ||'unkonwn';
	var arr_errmsg = str_errmsg.split('|');
	var errmsg = arr_errmsg[errindex] ? arr_errmsg[errindex]: arr_errmsg[0];
	var mode = element.attr('mode') || 1;
	var msgid= element.attr('msgid');
	var type=element.attr('type');
	(type!='checkbox' && type!='radio' && element.addClass(this['errinput']));
	if(mode == 1)
	{
		if(msgid)
		{
			id = '#' + msgid;
			$(id+'_state').removeClass('bg state_yes').addClass('bg state_no');
			$(id+'_msg').html(errmsg);
		}
		else
		{
			jQuery("<span tag='err' class='"+this['errcls']+"'></span>").html(errmsg).insertAfter(element);
		}
	}
	else
	{
		alert(errmsg);
	}
}

validator.removeErr =  function(element){
	element.removeClass(this['errinput']);
	element.parent('*').find('span[tag="err"]').remove();
}

validator.checkajax = function(element, datatype, errindex)
{
	var value=jQuery.trim(element.val());
	this['element'] = element;
	this['errindex'] = errindex;
	validator.removeErr(element);
	return eval(this[datatype]);
}

validator.checkDatatype = function(element,datatype){
	var value=jQuery.trim(element.val());
	this['element'] = element;
	validator.removeErr(element);
	switch(datatype){
		case "idCard" :
		case "date" :
		case "repeat" :
		case "repeat2" :
		case "range" :
		case "compare" :
        case "compareFloat":
		case "custom" :
		case "group" :
		case "limit" :
		case "limitB" :
		case "limitC" :
		case "limitD" :
		case "safeString" :
		case "filter" :
		return eval(this[datatype]);
		break;

		default:
			return this[datatype].test(value);
			break;
		}
}

validator.check=function(obj){
	var datatype = obj.attr('datatype');
	if(typeof(datatype) == "undefined") return true;

	if(obj.attr('require')!="true" && obj.val()=="") return true;
	var datatypes = datatype.split('|');
	var ok = true;

	jQuery.each(datatypes,function(index,data){
		if(typeof(validator[data]) == "undefined") {
			ok = false;
			return  false;
		}
		if(data != 'ajax')
		{
			if(validator.checkDatatype(obj,data)==false){
				validator.showErr(obj, index);
				return ok=false;
			}
			else
			{
				var msgid= obj.attr('msgid');
				if(msgid)
				{
					id = '#' + msgid;
					$(id+'_state').removeClass('bg state_no').addClass('bg state_yes');
					$(id+'_msg').html('');
				}
				else
				{

					jQuery("<span tag='err' class='yes'></span>").insertAfter(obj);
				}
			}
		}
		else
		{
			ok = validator.checkajax(obj, data, index);
		}
	});
	return ok;
}

jQuery.fn.checkForm = function(m, btn_id, callback){
	mode = (m==1) ? 1 : 0;
	var form=jQuery(this);
	var elements = form.find('input[require],select[require],textarea[require]');
	elements.unbind().blur(function(index){
		return validator.check(jQuery(this));
	});

	$('#'+btn_id).unbind().click(function(){
		var ok = true;
		var errIndex= new Array();
		var n=0;
		elements.each(function(i){
			if(validator.check(jQuery(this))==false){
				ok = false;
				errIndex[n++]=i;
			};
		});

		if(ok==false){
			elements.eq(errIndex[0]).focus().select();
			return false;
		}
		if(document.getElementById('video_uploader') && !upLoading)
		{
			uploadFile();
			return false;
		}
		// if($('#f_filed_1') && set_show==false)
		// {
			// $("select[@id=catids] option").each(function()
			// {
				// $(this).attr('selected','selected');
			// });
		// }
		if($('#hava_checked').val()==0)
		{
			YP_checkform();
			return false;
		}
		eval(callback);
		return true;
	});
}
jQuery.fn.checkInput = function() {
	return validator.check(jQuery(this));
}