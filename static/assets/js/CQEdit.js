function buildprevcreation(){
	container.innerHTML+=fcs;
	for (var a = 0; a < prevForm.length; a++) {
			container_count+=1;
			fcs=`<div>
            <form id="msform" method="post" action="" role="form">
              <fieldset>
                <h6 class="fs-title" name="Question${container_count}">Question${container_count}</h6>
                <input id="Q${container_count}" type="text" name="Question${container_count}" placeholder="Question${container_count}" class="question"/>
                <small id="emailHelp" class="form-text text-muted mb-2">Leave the remaining option fields empty, if not required.</small>
                <input id="Qa${container_count}" name="Qa${container_count}" type="text" placeholder="option a:" class="option mr-3"/>
                <input id="Qb${container_count}" name="Qb${container_count}" type="text" placeholder="option b:" class="option mr-3"/>
                <input id="Qc${container_count}" name="Qc${container_count}" type="text" placeholder="option c:" class="option mr-3"/>
                <input id="Qd${container_count}" name="Qd${container_count}" type="text" placeholder="option d:" class="option mr-3"/>
                <input id="Qe${container_count}" name="Qe${container_count}" type="text" placeholder="option e:" class="option mr-3"/>
                <input id="CorrectOption${container_count}" name="CorrectOption${container_count}" type="text" placeholder="Enter Correct Option a/b/c/d/e" class="correctOption">
                
              </fieldset>
            </form>
          </div>`;
		    container.innerHTML+=fcs;
	}
	for (var b = 1 ; b <= container_count; b++) {
		document.getElementById("Q".concat(b.toString())).value = prevForm[b-1].Question;
		document.getElementById("Qa".concat(b.toString())).value = prevForm[b-1].option1;
		document.getElementById("Qb".concat(b.toString())).value = prevForm[b-1].option2;
		document.getElementById("Qc".concat(b.toString())).value = prevForm[b-1].option3;
		document.getElementById("Qd".concat(b.toString())).value = prevForm[b-1].option4;
		document.getElementById("Qe".concat(b.toString())).value = prevForm[b-1].option5;
		document.getElementById("CorrectOption".concat(b.toString())).value = prevForm[b-1].Answer;
	}

	
}

function buildcreation(){
	container.innerHTML+=fcs;
	container_count+=1;
	fcs=`<div>
			  <form id="msform">
				<fieldset>
				  <h6 class="fs-title">Question ${container_count}</h6>
			  
				  <input id="Q${container_count}" type="text" name="Question${container_count}" placeholder="Question${container_count}" class="question"/>
				  <input id="Qa${container_count}" type="text" placeholder="option a:" />
				  <input id="Qb${container_count}" type="text" placeholder="option b:" />
				  <input id="Qc${container_count}" type="text" placeholder="option c:" />
				  <input id="Qd${container_count}" type="text" placeholder="option d:" />
				  <input id="Qe${container_count}" type="text" placeholder="option e:" />
				  <input id="CorrectOption${container_count}" type="text" placeholder="Enter Correct Option a/b/c/d/e">
				  
				</fieldset>
			  </form>
			</div>`;
	  
	container.innerHTML+=fcs;
	
  }
function addQ(){
	var values = [];
	var Qname = document.getElementById("Quizname").value;
	var Qdur = document.getElementById("Quiz_duration").value;
	var durtype = document.getElementById("TF").value;
	for (var i = 1; i <=container_count ; i++) {
		var ob = new Object();
		ob.question = document.getElementById("Q".concat(i.toString())).value;
		ob.options = new Object();
		ob.options.a = document.getElementById("Qa".concat(i.toString())).value;
		ob.options.b = document.getElementById("Qb".concat(i.toString())).value;
		ob.options.c = document.getElementById("Qc".concat(i.toString())).value;
		ob.options.d = document.getElementById("Qd".concat(i.toString())).value;
		ob.options.e = document.getElementById("Qe".concat(i.toString())).value;
		ob.CA = document.getElementById("CorrectOption".concat(i.toString())).value;
		values.push(ob);
	}

	container_count+=1;
	fcs=`<div>
	<form id="msform" >
	  <fieldset>
		<h6  class="fs-title">Question ${container_count}</h6>
	
		<input id="Q${container_count}" type="text" name="Question${container_count}" placeholder="Question${container_count}" class="question"/>
		<small id="emailHelp" class="form-text text-muted mb-2">Leave the remaining option fields empty, if not required.</small>
		<input id="Qa${container_count}" type="text" placeholder="option a:" class="option mr-3 " required/>
		<input id="Qb${container_count}" type="text" placeholder="option b:" class="option mr-3 " required/>
		<input id="Qc${container_count}" type="text" placeholder="option c:" class="option mr-3 "/>
		<input id="Qd${container_count}" type="text" placeholder="option d:" class="option mr-3 "/>
		<input id="Qe${container_count}" type="text" placeholder="option e:" class="option mr-3 "/>
		<input id="CorrectOption${container_count}" type="text" placeholder="Enter Correct Option a/b/c/d/e"
		class="correctOption ">
		
	  </fieldset>
	</form>
  </div>`;

		
	container.innerHTML+=fcs;
	document.getElementById("Quizname").value = Qname;
	document.getElementById("Quiz_duration").value = Qdur;
	document.getElementById("TF").value = durtype;


	for (var j = 1 ; j < container_count; j++) {
		document.getElementById("Q".concat(j.toString())).value = values[j-1].question;
		document.getElementById("Qa".concat(j.toString())).value = values[j-1].options.a;
		document.getElementById("Qb".concat(j.toString())).value = values[j-1].options.b;
		document.getElementById("Qc".concat(j.toString())).value = values[j-1].options.c;
		document.getElementById("Qd".concat(j.toString())).value = values[j-1].options.d;
		document.getElementById("Qe".concat(j.toString())).value = values[j-1].options.e;
		document.getElementById("CorrectOption".concat(j.toString())).value = values[j-1].CA;
	}
}
function save(){
	var quizform=[];
	quizform.push({quizname: document.getElementById("Quizname").value});
	quizform.push({quizduration: {time :document.getElementById("Quiz_duration").value,type : document.getElementById("TF").value}});
	for (var z = 1; z <= container_count; z++) {
		var obj = new Object();
		obj.question = document.getElementById("Q".concat(z.toString())).value;
		obj.answers = new Object();
		obj.answers.a = document.getElementById("Qa".concat(z.toString())).value;
		obj.answers.b = document.getElementById("Qb".concat(z.toString())).value;
		obj.answers.c = document.getElementById("Qc".concat(z.toString())).value;
		obj.answers.d = document.getElementById("Qd".concat(z.toString())).value;
		obj.answers.e = document.getElementById("Qe".concat(z.toString())).value;
		obj.correctAnswer = document.getElementById("CorrectOption".concat(z.toString())).value;
		quizform.push(obj);
	}
	var myjson = JSON.stringify(quizform);
	console.log(myjson);

	$.ajax({
		type: 'post',
		contentType: 'application/json; charset=utf-8',
		data: myjson,
		dataType: 'json',
		success: function (result) {
			alert(result.Result);
		}
	});
}



//variables
const container= document.getElementById("FC");

// variable containing previous form info to edit
const prevForm=JSON.parse(load_Questions());
const prevTime='0';
try{
	prevTime=JSON.parse(load_Time());
  }
catch{console.error();}
const prevMode=load_Mode();

var fcs=`<div>
<form class="row g-3" method="post" action="">
  <fieldset>
	<h2 class="fs-title">Quiz creation</h2>
	
	<div class="row g-3">
	<div class="col-sm-7">
		<input id="Quizname" type="Quizname" class="quizname form-control" name="Quiz_name" placeholder="Quiz Name" aria-label="City">
	</div>
	<div class="col-sm">
		<input id="Quiz_duration" type="text" name="quizduration" class=" Quiz_duration form-control" placeholder= "Enter Quiz Time" aria-label="State">
	</div>
	<div class="col-sm">
	<select id="TF" class="form-select" name="option">
	<option name="Hours" value="Hours">Hours</option>
   <option name="Minutes" value="Minutes">Minutes</option>
   <option name="Seconds" value="Seconds">Seconds</option>
	</select>
	</div>
	</div>
	</fieldset>
</form>
</div>`;
var container_count=0;
if(prevForm.length > 0){
	buildprevcreation();
  }
  else{buildcreation();}
function Mode( a,b){
	
	if(a=='Hours'){
		document.getElementsByName('quizduration')[0].value=b/(60*60);
      }
      else if(a=='Minutes'){
		document.getElementsByName('quizduration')[0].value=b/60;
      }
      else{
		document.getElementsByName('quizduration')[0].value=b;
      }
}
Mode(prevMode,prevTime);
document.getElementById('Quizname').value = load_Quiz();
document.getElementById('Quizname').disabled = true;
document.getElementsByName('quizduration')[0].value=load_Time();
console.log(load_Mode());
document.getElementById('TF').value=load_Mode();
const addQuestion = document.getElementById("add-question");
const savebutton = document.getElementById("save");
addQuestion.addEventListener('click', addQ);
savebutton.addEventListener('click',save);