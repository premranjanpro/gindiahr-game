/* GIndia Quest Engine — local, private progress for kids */
(function(){
  const KEY='gindiaQuestV2';
  const defaults={age:'6-8',xp:0,level:1,streak:0,bestStreak:0,quests:{},badges:[],games:{}};
  function state(){try{return Object.assign({},defaults,JSON.parse(localStorage.getItem(KEY)||'{}'));}catch(e){return Object.assign({},defaults);}}
  function save(s){localStorage.setItem(KEY,JSON.stringify(s));}
  function levelFor(xp){return Math.floor(xp/250)+1;}
  function award(game,correct,total,meta){
    const s=state(); const ratio=total?correct/total:0; if(ratio<0.7)return null;
    const tier=ratio>=1?'perfect':ratio>=0.9?'gold':'silver';
    const base=Math.round(correct*10+(meta&&meta.bonus||0)); const bonus=s.streak>=3?25:0; const gained=base+bonus;
    s.xp+=gained; s.level=levelFor(s.xp); s.streak++; s.bestStreak=Math.max(s.bestStreak,s.streak);
    const today=new Date().toISOString().slice(0,10); s.quests[today]=(s.quests[today]||0)+1;
    if(tier==='perfect'&&!s.badges.includes('perfect'))s.badges.push('perfect');
    if(s.streak>=5&&!s.badges.includes('streak5'))s.badges.push('streak5');
    s.games[game]={correct,total,ratio,tier,lastPlayed:Date.now()}; save(s);
    return {gained,level:s.level,streak:s.streak,tier,badge:s.badges[s.badges.length-1]||null};
  }
  function miss(){const s=state();s.streak=0;save(s);}
  function setAge(age){const s=state();s.age=age;save(s);}
  function get(){return state();}
  window.GIndiaQuest={award,miss,setAge,get,levelFor};
})();
