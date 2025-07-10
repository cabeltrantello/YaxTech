import React, { useState, useEffect, useCallback } from 'react';
import apiClient from './services/apiClient';
import Header from './components/Header';
import MockCard from './components/MockCard';
import MockForm from './components/MockForm';
import Notification from './components/Notification';
import { PlusCircle } from 'lucide-react';

function App() {
  const [activeMockDefinitions, setActiveMockDefinitions] = useState([]);
  const [isLoading, setIsLoading] = useState(true);
  const [isFormVisible, setIsFormVisible] = useState(false);
  const [mockToEdit, setMockToEdit] = useState(null);
  const [notification, setNotification] = useState({ message: '', type: '' });

  const fetchMocks = useCallback(async () => {
    try {
      setIsLoading(true);
      const response = await apiClient.get('/config');
      setActiveMockDefinitions(response.data);
    } catch (error) {
      console.error("Failed to fetch mock definitions:", error);
      setNotification({ message: 'Error fetching mocks.', type: 'error' });
    } finally {
      setIsLoading(false);
    }
  }, []);

  useEffect(() => {
    fetchMocks();
  }, [fetchMocks]);

  const handleShowNotification = (message, type) => {
    setNotification({ message, type });
  };

  const handleSaveMock = async (mock_payload_data) => {
    try {
      const isEditing = mockToEdit !== null;
      const mock_id_to_update = isEditing ? mockToEdit.mock_id : null;
      
      const request = isEditing
        ? apiClient.put(`/config/${mock_id_to_update}`, mock_payload_data)
        : apiClient.post('/config', mock_payload_data);

      await request;
      handleShowNotification(`Mock successfully ${isEditing ? 'updated' : 'created'}!`, 'success');
      setIsFormVisible(false);
      setMockToEdit(null);
      fetchMocks(); // Refresh the list
    } catch (error) {
      console.error("Failed to save mock:", error);
      handleShowNotification(error.response?.data?.detail || 'Failed to save mock.', 'error');
    }
  };
  
  const handleDeleteMock = async (mock_id_to_delete) => {
    if (window.confirm("Are you sure you want to delete this mock? This action cannot be undone.")) {
      try {
        await apiClient.delete(`/config/${mock_id_to_delete}`);
        handleShowNotification('Mock deleted successfully.', 'success');
        fetchMocks(); // Refresh the list
      } catch (error) {
        console.error("Failed to delete mock:", error);
        handleShowNotification('Failed to delete mock.', 'error');
      }
    }
  };

  const handleEditMock = (mock_definition_to_edit) => {
    setMockToEdit(mock_definition_to_edit);
    setIsFormVisible(true);
  };
  
  const handleAddNewMock = () => {
    setMockToEdit(null);
    setIsFormVisible(true);
  };

  return (
    <div className="min-h-screen bg-telco-dark-blue text-telco-white">
      <Header />
      <main className="p-8">
        <div className="flex justify-between items-center mb-6">
          <h2 className="text-3xl font-bold text-telco-white">Active Mock Definitions</h2>
          <button
            onClick={handleAddNewMock}
            className="flex items-center space-x-2 bg-telco-green text-telco-dark-blue px-4 py-2 rounded font-bold hover:bg-opacity-80 transition-colors"
          >
            <PlusCircle size={20} />
            <span>Add New Mock</span>
          </button>
        </div>

        {isLoading ? (
          <p className="text-telco-slate">Loading configurations...</p>
        ) : (
          <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-6">
            {activeMockDefinitions.map(mock => (
              <MockCard
                key={mock.mock_id}
                mock_definition_5g_core={mock}
                onEdit={handleEditMock}
                onDelete={handleDeleteMock}
              />
            ))}
          </div>
        )}

        {activeMockDefinitions.length === 0 && !isLoading && (
            <div className="text-center py-16 px-6 bg-telco-light-blue rounded-lg">
                <h3 className="text-xl text-telco-white">No Mocks Found</h3>
                <p className="text-telco-slate mt-2">Get started by creating your first mock definition.</p>
            </div>
        )}
      </main>

      {isFormVisible && (
        <MockForm
          mockToEdit={mockToEdit}
          onSave={handleSaveMock}
          onCancel={() => { setIsFormVisible(false); setMockToEdit(null); }}
        />
      )}
      
      <Notification 
        message={notification.message} 
        type={notification.type} 
        onClose={() => setNotification({ message: '', type: '' })}
      />
    </div>
  );
}

export default App;
