const host = 'https://coplant.duckdns.org/api';

export const register = (user) => {
    const response = fetch(`${host}/auth/register`, {
        method: 'POST',
        headers: {
            'Content-type': 'application/json; charset=UTF-8',
        },
        body: JSON.stringify(user),
    });
    return response;
};

export const login = (user) => {
    const response = fetch(`${host}/auth/login`, {
        method: 'POST',
        credentials: 'include',
        headers: {
            'Content-type': 'application/x-www-form-urlencoded',
        },
        body: new URLSearchParams(user),
    });
    return response;
};

export const logout = () => {
    const response = fetch(`${host}/auth/logout`, {
        method: 'POST',
        credentials: 'include',
    });
    return response;
};

export const userInfo = () => {
    const response = fetch(`${host}/users/me`, {
        credentials: 'include',
    });
    return response;
};

export const userChange = (user, inputs) => {
    const response = fetch(`${host}/users/me`, {
        method: 'PATCH',
        credentials: 'include',
        headers: {
            'Content-type': 'application/json; charset=UTF-8',
        },
        body: JSON.stringify({
            email: inputs[0].value.length == 0 ? user.email : inputs[0].value,
            password: inputs[1].value.length == 0 ? user.password : inputs[1].value,
            first_name:
                inputs[2].value.length == 0 ? user.firstName : inputs[2].value,
            middle_name:
                inputs[3].value.length == 0 ? user.middleName : inputs[3].value,
            last_name: inputs[4].value.length == 0 ? user.lastName : inputs[4].value,
        }),
    });
    return response;
};

export const getLoans = (user) => {
    const response = fetch(`${host}/loans/?user_id=${user.id}`, {
        credentials: 'include',
    });
    return response;
};

export const sendPassport = (passport, image) => {
    const response = fetch(`${host}/verify/?number=${passport}`, {
        method: 'POST',
        credentials: 'include',
        body: image,
    });
    return response;
};

export const newLoan = (inputs) => {
    const response = fetch(`${host}/loans/new`, {
        method: 'POST',
        credentials: 'include',
        headers: {
            'Content-type': 'application/json; charset=UTF-8',
        },
        body: JSON.stringify({
            period: inputs[7].value,
            amount: inputs[8].value,
        }),
    });
    return response;
};

export const operation = () => {
    const response = fetch(`${host}/operation`, {
        credentials: 'include',
    });
    return response;
};

export const loadPassport = (src) => {
    const response = fetch(`${host}/operation/photo/${src}`, {
        credentials: 'include',
    });
    return response;
};

export const verify = (src) => {
    const response = fetch(`${host}/operation/verify/${src}`, {
        credentials: 'include',
    });
    return response;
};

export const management = () => {
    const response = fetch(`${host}/management`, {
        credentials: 'include',
    });
    return response;
};

export const history = (user) => {
    const response = fetch(`${host}/management/history/${user}`, {
        credentials: 'include',
    });
    return response;
};

export const makeDecision = (id, decision) => {
    const response = fetch(
        `${host}/management/response/${id}?decision=${decision}`,
        {
            method: 'POST',
            credentials: 'include',
        }
    );
    return response;
};

export const accountant = () => {
    const response = fetch(`${host}/accountant`, {
        credentials: 'include',
    });
    return response;
};

export const pay = (id) => {
    const response = fetch(`${host}/accountant/pay/${id}`, {
        method: 'POST',
        credentials: 'include',
    });
    return response;
};

export const userInfoAdmin = (id) => {
    const response = fetch(`${host}/users/${id}`, {
        credentials: 'include',
    });
    return response;
};

export const userChangeAdmin = (user, inputs) => {
    const response = fetch(`${host}users/${user.id}`, {
        method: 'PATCH',
        credentials: 'include',
        headers: {
            'Content-type': 'application/json; charset=UTF-8',
        },
        body: JSON.stringify({
            email: inputs[1].value.length == 0 ? user.email : inputs[1].value,
            password: inputs[2].value.length == 0 ? user.password : inputs[2].value,
            first_name:
                inputs[3].value.length == 0 ? user.firstName : inputs[3].value,
            middle_name:
                inputs[4].value.length == 0 ? user.middleName : inputs[4].value,
            last_name: inputs[5].value.length == 0 ? user.lastName : inputs[5].value,
        }),
    });
    return response;
};

export const userDeleteAdmin = (id) => {
    const response = fetch(`${host}/users/${id}`, {
        method: 'DELETE',
        credentials: 'include',
        headers: {
            'Content-type': 'application/json; charset=UTF-8',
        },
    });
    return response;
};
