import firebase from 'firebase/app'

var firebaseConfig = {
    apiKey: "AIzaSyDtqv0MIbQEJVRT9GUyC7gyNGsIH4QZfQA",
    authDomain: "barter-system-8294d.firebaseapp.com",
    projectId: "barter-system-8294d",
    storageBucket: "barter-system-8294d.appspot.com",
    messagingSenderId: "31176058076",
    appId: "1:31176058076:web:a2293eec95df901b6b0019"
  };
  // Initialize Firebase
  firebase.initializeApp(firebaseConfig);

  export default firebase