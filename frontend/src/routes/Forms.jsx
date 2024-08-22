import React, { useEffect, useState } from "react"
import { useParams, useNavigate } from "react-router-dom"
import settings from "#settings"

const Forms = () => {
  const { id } = useParams();
  const navigate = useNavigate();
  const [formLinks, setFormLinks] = useState([]);

  useEffect(() => {
    (async () => {
      try {
        var response = await fetch(settings.API_URI);
        if (!response.ok) {
          throw new Error('Responce is not 200 ok')
        };   
        setFormLinks(await response.json());
      } catch (err){
        console.error(err)
      }
    })()});

  return (
    <ul>
      {formLinks.map((formPopulation) => {
        <li>
          <a href="">
            {assembleLink(formPopulation)}
          </a>
        </li>
      })}
    </ul>
  );
}


function assembleLink(formPopulation) {
  const link = `${settings.YANDEX_FORMS_URI}/${formPopulation.form_id}?`;
  for (let parameter in formPopulation.parameters) {
    link += `${parameter.field}=${parameter.answer}&`;
  }
  return link.slice(0, -1)
}

export default Forms;
