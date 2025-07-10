import React from 'react';
import { Edit, Trash2 } from 'lucide-react';

const MockCard = ({ mock_definition_5g_core, onEdit, onDelete }) => {
  const { mock_id, method, path, scenarios } = mock_definition_5g_core;

  const getMethodColor = (http_method) => {
    switch (http_method) {
      case 'GET': return 'text-green-400';
      case 'POST': return 'text-blue-400';
      case 'PUT': return 'text-yellow-400';
      case 'DELETE': return 'text-red-400';
      default: return 'text-telco-slate';
    }
  };

  return (
    <div className="bg-telco-light-blue p-4 rounded-lg shadow-md border border-gray-700 transition-transform hover:scale-105">
      <div className="flex justify-between items-start">
        <div>
          <span className={`font-mono font-bold text-lg ${getMethodColor(method)}`}>{method}</span>
          <p className="text-telco-light-slate font-mono break-all">{path}</p>
        </div>
        <div className="flex space-x-2">
          <button onClick={() => onEdit(mock_definition_5g_core)} className="p-2 text-telco-slate hover:text-telco-green transition-colors">
            <Edit size={18} />
          </button>
          <button onClick={() => onDelete(mock_id)} className="p-2 text-telco-slate hover:text-red-500 transition-colors">
            <Trash2 size={18} />
          </button>
        </div>
      </div>
      <div className="mt-3 pt-3 border-t border-gray-700">
        <h4 className="text-sm text-telco-slate mb-2">Scenarios ({Object.keys(scenarios).length})</h4>
        <div className="flex flex-wrap gap-2">
          {Object.keys(scenarios).map(scenario_name => (
            <span key={scenario_name} className="bg-gray-700 text-telco-light-slate text-xs font-mono px-2 py-1 rounded-full">
              {scenario_name}
            </span>
          ))}
        </div>
      </div>
    </div>
  );
};

export default MockCard;
