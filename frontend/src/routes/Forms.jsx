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
        console.log(response);
        setFormLinks(await response.json());
      } catch (err) {
        console.error(err)
        setFormLinks([]);
      }
    })()
  });

  return (
    <div>
      <h1>
        Анкты для проходения:
      </h1>
      <ul>
        {formLinks.map((formPopulation) => {
          return (
            <li>
              <a href={assembleLink(formPopulation)}>
                {assembleTitle(formPopulation)}
              </a>
            </li>
          )
        })}
      </ul>
    </div>
  );
}


function assembleLink(formPopulation) {
  var link = `${settings.YANDEX_FORMS_URI}/${formPopulation.form_id}?`;
  for (let parameter in formPopulation.parameters) {
    link += `${parameter.field}=${parameter.answer}&`;
  }
  return link.slice(0, -1);
}


function assembleTitle(formPopulation) {
  var title = '';
  for (let parameter in formPopulation.parameters) {
    title += `${parameter.field} = ${parameter.answer}\n`;
  }
  return title.slice(0, -1)
}

export default Forms;
