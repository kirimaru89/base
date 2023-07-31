import { atom } from 'recoil';

export const questionOptionsSt = atom({
    key: 'questionOptions',
    default: { type: [] }
});
