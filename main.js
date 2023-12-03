// main.js

// getter 학습하기

// 생성자 함수와 this 복습
// + JSDoc 주석 연습
/**
 * 생성자 함수를 통한 Dog 클래스의 인스턴스 생성 예제
 * @class
 */
class Dog {
  /**
   * Dog 클래스의 생성자 함수
   * @param {string} name - 개의 이름
   * @param {number} age - 개의 나이
   */
  constructor(name, age) {
    this.name = name;
    this.age = age;
  }
}