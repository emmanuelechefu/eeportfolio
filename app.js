const menu=document.querySelector('.menu'),nav=document.querySelector('nav');menu.addEventListener('click',()=>{const open=nav.classList.toggle('open');menu.setAttribute('aria-expanded',open);menu.textContent=open?'Close −':'Menu +'});
const modal=document.querySelector('dialog'),content=document.querySelector('#modal-content');document.querySelector('.close').onclick=()=>modal.close();modal.addEventListener('click',e=>{if(e.target===modal){const r=modal.getBoundingClientRect();if(e.clientX<r.left||e.clientX>r.right||e.clientY<r.top||e.clientY>r.bottom)modal.close()}});function show(title,body){content.innerHTML='<p class="modal-kicker">YOUR NAME / PORTFOLIO</p><h2 id="dialog-title">'+title+'</h2>'+body;modal.setAttribute('aria-labelledby','dialog-title');modal.showModal()}

// Full-word flowing color fields, strongly repelled by a nearby pointer, with fresh hover colors.
const portfolioWord=document.querySelector('.portfolio-word');
if(portfolioWord){
 const reducedMotion=window.matchMedia('(prefers-reduced-motion: reduce)');
 const finePointer=window.matchMedia('(hover: hover) and (pointer: fine)');
 const fields=Array.from({length:3},()=>({x:0,y:0}));
 let pointer=null,frame=0,previous=0,time=0,visible=true,ink=0,inkHue=0;
 function renderFlow(now){
  frame=0;
  const dt=previous?Math.min((now-previous)/1000,.05):0;
  previous=now;
  if(!reducedMotion.matches)time+=dt;
  const rect=portfolioWord.getBoundingClientRect();
  if(!rect.width||!rect.height)return;
  const follow=1-Math.exp(-dt*9);
  const px=pointer?pointer.x-rect.left:0,py=pointer?pointer.y-rect.top:0;
  const over=pointer&&finePointer.matches&&!reducedMotion.matches&&px>=0&&px<=rect.width&&py>=0&&py<=rect.height;
  ink+=((over?1:0)-ink)*(1-Math.exp(-dt*(over?12:2.8)));
  if(over){
   inkHue=(inkHue+dt*65)%360;
   portfolioWord.style.setProperty('--ink-x',(px/rect.width*100).toFixed(2)+'%');
   portfolioWord.style.setProperty('--ink-y',(py/rect.height*100).toFixed(2)+'%');
   portfolioWord.style.setProperty('--ink-hue',(345+Math.sin(inkHue*Math.PI/180+px/rect.width*2)*18).toFixed(2));
  }
  portfolioWord.style.setProperty('--ink-alpha',ink.toFixed(3));
  fields.forEach((field,i)=>{
   const phase=time*.38+i*2.1;
   const x=18+i*32+Math.sin(phase)*22;
   const y=50+Math.cos(phase*.83+i)*42;
   let pushX=0,pushY=0;
   if(pointer&&finePointer.matches&&!reducedMotion.matches){
    const dx=x/100*rect.width-(pointer.x-rect.left);
    const dy=y/100*rect.height-(pointer.y-rect.top);
    const distance=Math.hypot(dx,dy);
    const radius=Math.min(430,rect.width*.55+140);
    const force=Math.pow(Math.max(0,1-distance/radius),1.35)*290;
    pushX=(distance>1?dx/distance:Math.cos(i*2.1))*force;
    pushY=(distance>1?dy/distance:Math.sin(i*2.1))*force;
   }
   field.x+=(pushX-field.x)*follow;
   field.y+=(pushY-field.y)*follow;
   portfolioWord.style.setProperty('--flow-x'+i,(x+field.x/rect.width*100).toFixed(2)+'%');
   portfolioWord.style.setProperty('--flow-y'+i,(y+field.y/rect.height*100).toFixed(2)+'%');
  });
  if(!reducedMotion.matches&&visible&&!document.hidden)frame=requestAnimationFrame(renderFlow);
 }
 function startFlow(){if(!frame&&visible&&!document.hidden){previous=0;frame=requestAnimationFrame(renderFlow)}}
 function stopFlow(){cancelAnimationFrame(frame);frame=0;previous=0}
 document.addEventListener('pointermove',event=>{if(event.pointerType!=='touch')pointer={x:event.clientX,y:event.clientY}},{passive:true});
 document.documentElement.addEventListener('pointerleave',()=>{pointer=null});
 window.addEventListener('blur',()=>{pointer=null});
 document.addEventListener('visibilitychange',()=>document.hidden?stopFlow():startFlow());
 reducedMotion.addEventListener('change',()=>{stopFlow();ink=0;fields.forEach(f=>{f.x=0;f.y=0});startFlow()});
 finePointer.addEventListener('change',()=>{pointer=null});
 if('IntersectionObserver' in window)new IntersectionObserver(entries=>{visible=entries[0].isIntersecting;visible?startFlow():stopFlow()}).observe(portfolioWord);
 startFlow();
}
