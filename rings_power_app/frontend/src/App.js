import React, { useState } from 'react';
import 'bootstrap/dist/css/bootstrap.min.css';
import { Table, Form } from 'react-bootstrap';

function App() {
  const [nomeUsuario, setNomeUsuario] = useState('');
  const [nomeFilme, setNomeFilme] = useState('');
  const [resultado, setResultado] = useState([]);
  const [historyData, setHistoryData] = useState([]);
  const [isLoading, setIsLoading] = useState(false);
  const [activeTab, setActiveTab] = useState('buscar');
  const [filterUser, setFilterUser] = useState('');
  const [filterName, setFilterName] = useState('');

  const handleNomeUsuarioChange = (event) => {
    setNomeUsuario(event.target.value);
  };

  const handleNomeFilmeChange = (event) => {
    setNomeFilme(event.target.value);
  };

  const handleBuscar = async () => {
    const response = await fetch(`http://0.0.0.0:8000/movies/?name=${nomeFilme}&user=${nomeUsuario}`);
    const dados = await response.json();
    setResultado(dados);
  };

  const handleHistory = async () => {
    setIsLoading(true);
    try {
      const response = await fetch('http://0.0.0.0:8000/history/');
      const data = await response.json();
      setHistoryData(data);
    } catch (error) {
      console.error('Error fetching history:', error);
    } finally {
      setIsLoading(false);
    }
  };

  const filteredHistoryData = historyData.filter((entry) => {
    return entry.user.toLowerCase().includes(filterUser.toLowerCase()) &&
           entry.name.toLowerCase().includes(filterName.toLowerCase());
  });

  const handleUserFilterChange = (event) => {
    setFilterUser(event.target.value);
  };

  const handleNameFilterChange = (event) => {
    setFilterName(event.target.value);
  };

  const displayHistory = () => {
    return (
      <div className="history">
        {isLoading ? (
          <p>Carregando...</p>
        ) : (
          <Table striped bordered hover>
            <thead>
              <tr>
                <th>User</th>
                <th>Name</th>
                <th>Academy Award Wins</th>
                <th>Timestamp</th>
              </tr>
              <tr>
                <th>
                  <Form.Control
                    type="text"
                    placeholder="Filtrar por usuário"
                    value={filterUser}
                    onChange={handleUserFilterChange}
                  />
                </th>
                <th>
                  <Form.Control
                    type="text"
                    placeholder="Filtrar por nome"
                    value={filterName}
                    onChange={handleNameFilterChange}
                  />
                </th>
              </tr>
            </thead>
            <tbody>
              {filteredHistoryData.map((entry) => (
                <tr key={entry.timestamp}>
                  <td>{entry.user}</td>
                  <td>{entry.name}</td>
                  <td>{entry.academyAwardWins}</td>
                  <td>{entry.timestamp}</td>
                </tr>
              ))}
            </tbody>
          </Table>
        )}
      </div>
    );
  };

  return (
    <div className="App container">
      <h3 className="mt-4">O Senhor dos Anéis</h3>
      <h5 className="mt-4">Ash nazg durbatulûk, ash nazg gimbatul, ash nazg thrakatulûk agh burzum-ishi krimpatul.</h5>
      <h6 className="mt-4">Um anel para a todos governar, um anel para encontrá-los, um anel para a todos trazer e na escuridão aprisioná-los.</h6>

      <ul className="nav nav-tabs mt-4">
        <li className="nav-item">
          <button
            className={`nav-link ${activeTab === 'buscar' ? 'active' : ''}`}
            onClick={() => setActiveTab('buscar')}
          >
            Buscar
          </button>
        </li>
        <li className="nav-item">
          <button
            className={`nav-link ${activeTab === 'historico' ? 'active' : ''}`}
            onClick={() => { setActiveTab('historico'); handleHistory(); }}
          >
            Consultar histórico
          </button>
        </li>
      </ul>

      <div className="tab-content mt-4">
        {activeTab === 'buscar' && (
          <div className="tab-pane fade show active">
            <div className="form-group">
              <label htmlFor="nomeUsuario">Seu Nome:</label>
              <input type="text" className="form-control" id="nomeUsuario" value={nomeUsuario} onChange={handleNomeUsuarioChange} />
            </div>
            <div className="form-group">
              <label htmlFor="nomeFilme">Nome do Filme:</label>
              <input type="text" className="form-control" id="nomeFilme" value={nomeFilme} onChange={handleNomeFilmeChange} />
            </div>
            <button type="button" className="btn btn-primary" onClick={handleBuscar}>Buscar</button>

            <div className="resultados mt-4">
              {resultado.map((filme) => (
                <div key={filme.name} className="filme-card card mb-3">
                  <div className="card-body">
                    <h2 className="card-title">{filme.name}</h2>
                    <p className="card-text">Premiações do Oscar:</p>
                    <ul className="list-group list-group-flush">
                      <li className="list-group-item">Nomeações: {filme.academyAwardNominations}</li>
                      <li className="list-group-item">Vitórias: {filme.academyAwardWins}</li>
                    </ul>
                  </div>
                </div>
              ))}
            </div>
          </div>
        )}

        {activeTab === 'historico' && (
          <div className="tab-pane fade show active">
            <div className="history-button mt-4">
              <button type="button" className="btn btn-info" onClick={handleHistory}>Consultar histórico</button>
            </div>
            {displayHistory()}
          </div>
        )}
      </div>
    </div>
  );
}

export default App;
