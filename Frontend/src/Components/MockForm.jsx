import React, { useState, useEffect } from 'react';
import JSONInput from 'react-json-editor-ajrm';
import locale from 'react-json-editor-ajrm/locale/en';

const MockForm = ({ mockToEdit, onSave, onCancel }) => {
  const [method, setMethod] = useState('GET');
  const [path, setPath] = useState('');
  const [scenarios, setScenarios] = useState({
    default: { status_code: 200, headers: {}, body: { message: "ok" } }
  });
  const [error, setError] = useState(null);

  const isEditing = mockToEdit !== null;

  useEffect(() => {
    if (isEditing) {
      setMethod(mockToEdit.method);
      setPath(mockToEdit.path);
      setScenarios(mockToEdit.scenarios);
    }
  }, [mockToEdit, isEditing]);

  const handleSave = (e) => {
    e.preventDefault();
    if (!path.startsWith('/')) {
      setError("Path must start with a '/'.");
      return;
    }
    if (!scenarios.default) {
      setError("A 'default' scenario is required.");
      return;
    }
    setError(null);
    onSave({ method, path, scenarios });
  };

  return (
    <div className="fixed inset-0 bg-black bg-opacity-75 flex items-center justify-center z-50">
      <div className="bg-telco-light-blue w-full max-w-3xl p-6 rounded-lg shadow-2xl border border-gray-700">
        <h2 className="text-2xl font-bold text-telco-white mb-4">
          {isEditing ? 'Edit Mock Definition' : 'Create New Mock Definition'}
        </h2>
        <form onSubmit={handleSave}>
          <div className="grid grid-cols-3 gap-4 mb-4">
            <div className="col-span-1">
              <label className="block text-sm font-bold text-telco-slate mb-2" htmlFor="method">
                HTTP Method
              </label>
              <select
                id="method"
                value={method}
                onChange={(e) => setMethod(e.target.value)}
                className="w-full bg-gray-700 text-telco-white p-2 rounded border border-gray-600 focus:outline-none focus:ring-2 focus:ring-telco-green"
              >
                <option>GET</option>
                <option>POST</option>
                <option>PUT</option>
                <option>DELETE</option>
                <option>PATCH</option>
              </select>
            </div>
            <div className="col-span-2">
              <label className="block text-sm font-bold text-telco-slate mb-2" htmlFor="path">
                Endpoint Path
              </label>
              <input
                id="path"
                type="text"
                value={path}
                onChange={(e) => setPath(e.target.value)}
                placeholder="/api/v1/network-elements/bbu-1/status"
                className="w-full bg-gray-700 text-telco-white p-2 rounded border border-gray-600 focus:outline-none focus:ring-2 focus:ring-telco-green font-mono"
                required
              />
            </div>
          </div>
          <div className="mb-4">
            <label className="block text-sm font-bold text-telco-slate mb-2">
              Scenarios (JSON)
            </label>
            <JSONInput
              id="scenarios-editor"
              placeholder={scenarios}
              locale={locale}
              colors={{
                default: '#ccd6f6', // telco-white
                background: '#0A192F', // telco-dark-blue
                string: '#64ffda', // telco-green
                number: '#FFC700',
                colon: '#8892b0', // telco-slate
                keys: '#a8b2d1', // telco-light-slate
                error: '#F97583',
              }}
              style={{
                outerBox: { border: '1px solid #4A5568', borderRadius: '0.5rem' },
                body: { fontFamily: 'monospace' }
              }}
              onChange={(data) => data.jsObject && setScenarios(data.jsObject)}
              height="250px"
              width="100%"
            />
          </div>
          {error && <p className="text-red-500 text-sm mb-4">{error}</p>}
          <div className="flex justify-end space-x-4">
            <button
              type="button"
              onClick={onCancel}
              className="bg-gray-600 text-telco-white px-4 py-2 rounded hover:bg-gray-700 transition-colors"
            >
              Cancel
            </button>
            <button
              type="submit"
              className="bg-telco-green text-telco-dark-blue px-4 py-2 rounded font-bold hover:bg-opacity-80 transition-colors"
            >
              {isEditing ? 'Save Changes' : 'Create Mock'}
            </button>
          </div>
        </form>
      </div>
    </div>
  );
};

export default MockForm;
