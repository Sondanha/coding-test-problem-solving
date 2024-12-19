function solution(myStr) {
    const splited = myStr.split(/[abc]/);
    const answer = splited.filter((elem)=>{return elem.length !== 0})
    return answer.length === 0 ? ['EMPTY'] : answer
}