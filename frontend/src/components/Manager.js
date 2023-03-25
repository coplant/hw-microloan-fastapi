import React, {useEffect, useState} from 'react';
import {useNavigate} from 'react-router-dom';
import {history, logout, makeDecision, management} from '../APIs';

function Manager() {
  const navigate = useNavigate();
  const [users, setUsers] = useState([]);
  const [loans, setLoans] = useState([]);
  useEffect(() => {
    management()
        .then((response) => response.json())
        .then((res) => {
          setLoans(res.data);
        });
  }, []);

  const handleLogout = async () => {
    const response = await logout();
    const res = await response.json();
    if (response.ok == true) {
      navigate('/login');
    } else {
      alert(res.detail);
    }
  };

  const handleMore = async (user) => {
    if (users.length != 0) {
      setUsers([]);
    } else {
      const response = await history(user);
      const res = await response.json();
      setUsers(res.data);
    }
    const colorized = document.querySelector(`tr[id='${user}']`);
    colorized.classList.toggle('bg-orange-700');
  };

  const handleSubmit = async (id, decision) => {
    let response = await makeDecision(id, decision);
    let res = await response.json();
    if (response.ok == true) {
      alert('Your decision has been sent');
      response = await management();
      res = await response.json();
      setLoans(res.data);
    } else {
      alert(res.detail);
    }
  };
  return (
      <>
        <nav className='bg-orange-300 border-gray-200 px-4 lg:px-6 py-2.5'>
          <div className='flex flex-wrap justify-end items-center mx-auto max-w-screen-xl'>
            <button
                onClick={handleLogout}
                className='bg-orange-500 hover:bg-orange-400 text-white font-bold py-2 px-4 border-b-4 border-orange-700 hover:border-orange-500 rounded mr-2 w-1/6 text-center'
            >
              Log Out
            </button>
          </div>
        </nav>
        <div className='bg-orange-200 min-h-screen'>
          <h2 className='text-2xl font-bold text-center text-white pt-10 mb-5'>
            Manager menu
          </h2>
          {loans.length == 0 ? null : (
              <div className='overflow-x-auto  sm:rounded-lg mx-5'>
                <table className='w-full text-sm text-left text-white '>
                  <thead className='text-xs text-white uppercase bg-orange-500'>
                  <tr>
                    <th className='px-6 py-3'>Creation Date</th>
                    <th className='px-6 py-3'>End Date</th>
                    <th className='px-6 py-3'>Status</th>
                    <th className='px-6 py-3'>Period</th>
                    <th className='px-6 py-3'>Amount</th>
                    <th className='px-6 py-3'>More</th>
                    <th className='px-6 py-3'>Confirm</th>
                    <th className='px-6 py-3'>Reject</th>
                  </tr>
                  </thead>
                  <tbody>
                  {loans.map((loan) => (
                      <tr
                          id={loan.user_id}
                          key={loan.user_id}
                          className='bg-orange-400'
                      >
                        <td className='px-6 py-4'>{loan.creation_date}</td>
                        <td className='px-6 py-4'>
                          {loan.end_date == null ? 'NULL' : loan.end_date}
                        </td>
                        <td className='px-6 py-4'>{loan.status}</td>
                        <td className='px-6 py-4'>{loan.period}</td>
                        <td className='px-6 py-4'>{loan.amount}</td>
                        <td className='cursor-pointer'>
                          <button
                              className='w-full h-12'
                              onClick={() => {
                                handleMore(loan.user_id);
                              }}
                          >
                            About User
                          </button>
                        </td>
                        <td className='cursor-pointer bg-green-500  ml-2 hover:bg-green-700'>
                          <button
                              className='w-full h-12'
                              onClick={() => {
                                handleSubmit(loan.user_id, true);
                              }}
                          >
                            Confirm
                          </button>
                        </td>
                        <td className='cursor-pointer bg-red-500 hover:bg-red-700'>
                          <button
                              className='w-full h-12'
                              onClick={() => {
                                handleSubmit(loan.user_id, false);
                              }}
                          >
                            Reject
                          </button>
                        </td>
                      </tr>
                  ))}
                  </tbody>
                </table>
              </div>
          )}
          {users.length == 0 ? null : (
              <div className='overflow-x-auto  sm:rounded-lg mx-5 w-1/2 mt-10'>
                <table className='w-full text-sm text-left text-white '>
                  <thead className='text-xs text-white uppercase bg-orange-300'>
                  <tr>
                    <th className='px-6 py-3'>Name</th>
                    <th className='px-6 py-3'>Last Name</th>
                    <th className='px-6 py-3'>Middle Name</th>
                    <th className='px-6 py-3'>passport</th>
                    <th className='px-6 py-3'>Period</th>
                    <th className='px-6 py-3'>Amount</th>
                  </tr>
                  </thead>
                  <tbody>
                  {users.map((user) => (
                      <tr key={user.id} className='bg-orange-300'>
                        <td className='px-6 py-4'>{user.first_name}</td>
                        <td className='px-6 py-4'>{user.last_name}</td>
                        <td className='px-6 py-4'>{user.middle_name}</td>
                        <td className='px-6 py-4'>{user.passport}</td>
                        <td className='px-6 py-4'>{user.period}</td>
                        <td className='px-6 py-4'>{user.amount}</td>
                      </tr>
                  ))}
                  </tbody>
                </table>
              </div>
          )}
        </div>
      </>
  );
}
export default Manager;