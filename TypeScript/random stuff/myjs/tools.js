export function print(...value) {
    if (typeof value === "undefined") {
        console.log("");
        return;
    }
    console.log(...value);
}
export function greet(name, list = null) {
    console.log(name);
    if (list === null) {
        return;
    }
    for (let i = 0; i < list.length; i++) {
        console.log(list[i]);
    }
}
const counter = () => {
    let score = 0;
    let ok = true;
    function dincrease() {
        score--;
        return score;
    }
    function increase() {
        score++;
        return score;
    }
    return { score, ok, increase, dincrease };
};
export const NOTE = "Don't give up now, keep going ";
export default counter;
//# sourceMappingURL=tools.js.map