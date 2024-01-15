skill=1
const addskill = document.getElementById("addskill")
const remskill = document.getElementById("remskill")

addskill.addEventListener('click',function () {
    let form_test = remskill.nextElementSibling
    
    let test = document.createElement('input')


    test.setAttribute("class","form-control mt-2")
    test.setAttribute("name","skill"+skill)
    skill++
    form_test.append(test)
    remskill.hidden=false
    
})
remskill.addEventListener('click',function () {
    let lastDive = remskill.nextElementSibling.lastChild
    console.log(lastDive)
    skill--
    lastDive.remove()
    if(skill===1)
    {
        remskill.hidden=true
    }    
})


achieve=1
const addachieve = document.getElementById("addachieve")
const remachieve = document.getElementById("remachieve")

addachieve.addEventListener('click',function () {
    let form_test = remachieve.nextElementSibling
    
    let test = document.createElement('input')


    test.setAttribute("class","form-control mt-2")
    test.setAttribute("name","achievement"+achieve)
    achieve++
    form_test.append(test)
    remachieve.hidden=false
    
})
remachieve.addEventListener('click',function () {
    let lastDive = remachieve.nextElementSibling.lastChild
    console.log(lastDive)
    achieve--
    lastDive.remove()
    if(achieve===1)
    {
        remachieve.hidden=true
    }
})



project=1
const addproject = document.getElementById("addproject")
const remproject = document.getElementById("remproject")

addproject.addEventListener('click',function () {
    let form_test = remproject.parentElement
    
    let test = document.createElement('div')
    test.innerHTML=`
                                <div class="form-group mt-2">
                                    <label for="">Project Name</label>
                                    <input name="projectname${project}" class="form-control">
                                </div>
                                <div class="form-group mt-2">
                                    <label for="">Description</label>
                                    <textarea name="projectdesc${project}" class="form-control mb-5"></textarea>
                                </div>`


    project++
    form_test.append(test)
    remproject.hidden=false
    
})
remproject.addEventListener('click',function () {
    let lastDive = remproject.parentElement.lastChild
    console.log(lastDive)
    project--
    lastDive.remove()
    if(project===1)
    {
        remproject.hidden=true
    }    
})



experience=1
const addexperience = document.getElementById("addexperience")
const remexperience = document.getElementById("remexperience")

addexperience.addEventListener('click',function () {
    let form_test = remexperience.parentElement
    
    let test = document.createElement('div')
    // test.setAttribute("class","container bg-primary")
    test.innerHTML=`
    <div class="form-group mt-2">
                                    <label for="">Company Name</label>
                                    <input name="company${experience}" class="form-control m-2">
                                </div>
                            </div>

                            <div class="form-group mt-2">
                                <label for="">Role</label>
                                <input name="role${experience}" class="form-control m-2">
                            </div>

                            <div class="form-group mt-2">
                                <label for="">Start Date</label>
                                <input name="startdate${experience}" type="date" class="form-control m-2">
                            </div>

                            <div class="form-group mt-2">
                                <label for="">End Date</label>
                                <input name="enddate${experience}" type="date" class="form-control m-2">
                            </div>
                            <div class="form-group mt-2">
                                <label for="">Description</label>
                                <textarea name="description${experience}" class="form-control mb-4"></textarea>

                            </div>
    `


    experience++
    form_test.append(test)
    remexperience.hidden=false
    
})
remexperience.addEventListener('click',function () {
    let lastDive = remexperience.parentElement.lastChild
    console.log(lastDive)
    experience--
    lastDive.remove()
    if(experience===1)
    {
        remexperience.hidden=true
    }    
})




social=1
const addsocial = document.getElementById("addsocial")
const remsocial = document.getElementById("remsocial")

addsocial.addEventListener('click',function () {
    let form_test = remsocial.parentElement
    
    let test = document.createElement('div')
    test.innerHTML=`<div class="form-group mt-2">
    <label for="">Social Name</label>
    <input name="socialname${social}" class="form-control">
</div>
<div class="form-group mt-2">
    <label for="">Profile Link</label>
    <input name="sociallink${social}" class="form-control">
</div>`


    social++
    form_test.append(test)
    remsocial.hidden=false
    
})
remsocial.addEventListener('click',function () {
    let lastDive = remsocial.parentElement.lastChild
    console.log(lastDive)
    social--
    lastDive.remove()
    if(social===1)
    {
        remsocial.hidden=true
    }    
})



lang=1
const addlang = document.getElementById("addlang")
const remlang = document.getElementById("remlang")

addlang.addEventListener('click',function () {
    let form_test = remlang.nextElementSibling
    
    let test = document.createElement('input')


    test.setAttribute("class","form-control mt-4")
    test.setAttribute("name","lang"+lang)
    lang++
    form_test.append(test)
    remlang.hidden=false
    
})
remlang.addEventListener('click',function () {
    let lastDive = remlang.nextElementSibling.lastChild
    console.log(lastDive)
    lang--
    lastDive.remove()
    if(lang===1)
    {
        remlang.hidden=true
    }    
})


const addpg = document.getElementById("addpg")
const rempg = document.getElementById("rempg")

addpg.addEventListener('click',function () {
    let form_test = rempg.parentElement
    
    let test = document.createElement('div')
    test.innerHTML=`
    <div class="form-group mt-2">
                                        <label for="">College Name</label>
                                        <input required name="pgcollege" class="form-control">
                                    </div>
    
                                    <div class="form-group mt-2">
                                        <label for="">Course Name</label>
                                        <input required name="pgcourse" placeholder="Bachelor of" class="form-control">
                                    </div>
    
                                    <div class="form-group mt-2">
                                        <label for="">CGPA</label>
                                        <input required type="number" name="pgscore" placeholder="CGPA" class="form-control mb-3">
                                    </div>
    `

    form_test.append(test)
    rempg.hidden=false
    addpg.hidden=true
    
})

rempg.addEventListener('click',function () {

    let lastDive = rempg.parentElement.lastChild
    lastDive.remove()
    rempg.hidden=true
    addpg.hidden=false


    
})
