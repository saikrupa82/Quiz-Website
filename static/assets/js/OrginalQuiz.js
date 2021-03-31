(function(){
  // Functions

  function startTimer(seconds){
    var h5 = document.getElementsByTagName("h5");
    h5[0].innerHTML = "EXAM ENDS IN";

    var sec         = seconds,
        countDiv    = document.getElementById("timer"),
        secpass,
        countDown   = setInterval(function () {
            'use strict';
            
            secpass();
        }, 1000);

    function secpass() {
        'use strict';
        
        var min     = Math.floor(sec / 60),
            remSec  = sec % 60;
        
        if (remSec < 10) {
            
            remSec = '0' + remSec;
        
        }
        if (min < 10) {
            
            min = '0' + min;
        
        }
        countDiv.innerHTML = min + ":" + remSec;
        
        if (sec > 0) {
            
            sec = sec - 1;
            
        } else {
            
            clearInterval(countDown);
            
            countDiv.innerHTML = 'countdown done';
            
        }
    }
  }
  function addBT(x){
    var btn = document.createElement("BUTTON");
    var s='0';
    var fs=x.toString();
    btn.id=fs;
    if((x/10)<1){
      var res=s.concat(fs);
      btn.innerHTML = res;
    }
    else{
      btn.innerHTML = x;
    }
    
    
    btn.addEventListener("click", showSlide.bind(null,x-1));
    document.getElementById("status").appendChild(btn);
  }
  function buildQuiz(){
    // variable to store the HTML output
    const output = [];

    // for each question...
    myQuestions.forEach(
      (currentQuestion, questionNumber) => {

        // variable to store the list of possible answers
        const answers = [];

        // and for each available answer...
        var count=0;
        for(letter in currentQuestion.answers){

          // ...add an HTML radio button
          answers.push(
            `<label>
              <input type="radio" name="question${questionNumber}" id="question${questionNumber}${count}" value="${letter}">
              ${letter} :
              ${currentQuestion.answers[letter]}
            </label>`
          );
          count=count+1;
        }
        addBT(questionNumber+1);
        flaglist.push(0);
        // add this question and its answers to the output
        output.push(
          `<div class="slide">
            <div class="question"> ${currentQuestion.question} </div>
            <div class="answers"> ${answers.join("")} </div>
          </div>`
        );
      }
    );

    // finally combine our output list into one string of HTML and put it on the page
    quizContainer.innerHTML = output.join('');
  }

  function saveResults(){

    // gather answer containers from our quiz
    const answerContainers = quizContainer.querySelectorAll('.answers');
    var user_Answers={}
    // keep track of user's answers
    //let numCorrect = 0;

    // for each question...
    myQuestions.forEach( (currentQuestion, questionNumber) => {

      // find selected answer
      const answerContainer = answerContainers[questionNumber];
      const selector = `input[name=question${questionNumber}]:checked`;
      const userAnswer = (answerContainer.querySelector(selector) || {}).value;
      user_Answers[questionNumber+1]=userAnswer;
      // if answer is correct
      //if(userAnswer === currentQuestion.correctAnswer){
        // add to the number of correct answers
       // numCorrect++;

        // color the answers green
        //answerContainers[questionNumber].style.color = 'green';
      //}
      // if answer is wrong or blank
     // else{
        // color the answers red
       // answerContainers[questionNumber].style.color = 'red';
      //}
    });

    // show number of correct answers out of total
    //resultsContainer.innerHTML = `${numCorrect} out of ${myQuestions.length}`;
    
    user_Answers=JSON.stringify(user_Answers);
    $.ajax({
      type: 'post',
      contentType: 'application/json; charset=utf-8',
      data: user_Answers,
      dataType: 'json',
      success: function (result) {
        console.log(result.Result)
        alert(result.Result);
      }
    });
  
  }
  
  function showSlide(n) {
    slides[currentSlide].classList.remove('active-slide');
    slides[n].classList.add('active-slide');
    currentSlide = n;
    if(currentSlide === 0){
      previousButton.style.display = 'none';
    }
    else{
      previousButton.style.display = 'inline-block';
    }
    if(currentSlide === slides.length-1){
      nextButton.style.display = 'none';
      
    }
    else{
      nextButton.style.display = 'inline-block';
    }
  }
  /*
    cs+y:- Actual current slide.
    cs+y+1:- Slide id/question-number.
  */
  function updateStatus(cs,y){
    const answerContainers = quizContainer.querySelectorAll('.answers');
    const answerContainer = answerContainers[cs+y];
    const selector = `input[name=question${cs+y}]:checked`;
    const userAnswer = (answerContainer.querySelector(selector) || {}).value;
    const bt=document.getElementById((cs+y+1).toString());
    if (typeof userAnswer !== "undefined" && flaglist[cs+y]!=1){
        bt.style.backgroundColor = "#7ae673";/*green*/
        bt.style.color="#ffffff";
    }
    if (typeof userAnswer === "undefined" && flaglist[cs+y]==1){
        bt.style.backgroundColor = "#ff6161";/*red*/
        bt.style.color="#ffffff";
    }
    if (typeof userAnswer !== "undefined" && flaglist[cs+y]==1){
        bt.style.backgroundColor = "#ffbe73";/*orange*/
    }
    if (typeof userAnswer === "undefined" && flaglist[cs+y]!=1){
        bt.style.backgroundColor = "#c9c9c9"; 
    }
  }
  function flagit(fs){
    if (flaglist[fs]==0){
      flaglist[fs]=1;
    }
    else{
      flaglist[fs]=0;
    }
    updateStatus(currentSlide,0);
    
  }


  function clearslide(cs){
    /*Get obj size*/
    Object.size = function(obj) {
        var size = 0, key;
        for (key in obj) {
            if (obj.hasOwnProperty(key)) size++;
        }
        return size;
    };
    /*Get no of options for current slide*/
    Qans = Object.size(myQuestions[cs].answers);
    /*uncheck/clear option*/
    for (var i = 0; i < Qans; i++) {
      document.getElementById("question".concat(cs,i)).checked = false;
    } 
    
    updateStatus(currentSlide,0);
  }


  function clear(){
    clearslide(currentSlide.toString());
  }
  function flag(){
    flagit(currentSlide);
  }
  function showNextSlide() {
    showSlide(currentSlide + 1);
    updateStatus(currentSlide,-1);
  }

  function showPreviousSlide() {
    showSlide(currentSlide - 1);
    updateStatus(currentSlide,1);
  }

  // Variables
  const quizContainer = document.getElementById('quiz');
  const resultsContainer = document.getElementById('results');
  const submitButton = document.getElementById('submit');



var fo=JSON.parse(load_Questions());

  var qo=[];
  var ops=['a','b','c','d','e'];
  function fo_to_qo(qa,index){
    ob={};
    ob.question=((index+1).toString()).concat(".".concat(qa.Question));
    ob.answers={};
    for (var i = 0; i <Object.keys(qa).length-1; i++) {
      opstr='option'.concat((i+1).toString());
      if(qa[opstr]!=""){
        ob.answers[ops[i]]=qa[opstr];
      }
    }
    
    qo.push(ob);
  }
  for (var k = 0; k <fo.length; k++) {
    fo_to_qo(fo[k],k);
  }

  const myQuestions= qo;
  const mq = load_Questions();

  const timelimit=JSON.parse(load_Time());
  var flaglist=[];
  var statusSlide = 0;
  // Kick things off
  buildQuiz();
  startTimer(timelimit);
  // Pagination
  const previousButton = document.getElementById("previous");
  const nextButton = document.getElementById("next");
  const slides = document.querySelectorAll(".slide");
  const flagbutton= document.getElementById("flag");
  const clearbutton= document.getElementById("clear");
  let currentSlide = 0;

  // Show the first slide
  showSlide(currentSlide);

  // Event listeners
  submitButton.addEventListener('click', saveResults);
  previousButton.addEventListener("click", showPreviousSlide);
  nextButton.addEventListener("click", showNextSlide);
  flagbutton.addEventListener("click", flag);
  clearbutton.addEventListener("click", clear);
})();


// $(window).load(function () {
//   $(".trigger_popup_fricc").click(function(){
//      $('.hover_bkgr_fricc').show();
//   });
//   $('.hover_bkgr_fricc').click(function(){
//       $('.hover_bkgr_fricc').hide();
//   });
//   $('.popupCloseButton').click(function(){
//       $('.hover_bkgr_fricc').hide();
//   });
// });
