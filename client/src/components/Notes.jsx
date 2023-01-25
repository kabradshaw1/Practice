import {useState, useEffect} from "react"
import axios from "axios"
import List from "./List"

function Note() {
  const [notes , setNewNotes] = useState(null)
  const [formNote, setFormNote] = useState({
        title: "",
        content: ""
        })
  }